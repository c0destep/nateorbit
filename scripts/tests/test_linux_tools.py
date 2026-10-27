"""Exercise failure modes of the read-only Linux doctor and setup wrapper."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('doctor', ROOT / 'scripts/doctor.py')
doctor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(doctor)


class LinuxToolsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='nateorbit tools ')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'scripts').mkdir()
        (self.root / 'scripts/android-env.json').write_text((ROOT / 'scripts/android-env.json').read_text())

    def test_sdk_env_precedence_and_escaped_properties(self):
        (self.root / 'local.properties').write_text('sdk.dir=/a\\ path/sdk\\:one\n')
        self.assertEqual(doctor.sdk_location({}, self.root), Path('/a path/sdk:one'))
        self.assertEqual(doctor.sdk_location({'ANDROID_HOME': '/primary', 'ANDROID_SDK_ROOT': '/old'}, self.root), Path('/primary'))

    def test_wrong_runtime_or_missing_compiler_fails(self):
        with patch.object(doctor, 'java_major', side_effect=[21, None]):
            self.assertFalse(doctor.inspect({}, self.root, jdk_only=True)[0]['ok'])
        with patch.object(doctor, 'java_major', return_value=17):
            self.assertFalse(doctor.inspect({}, self.root, jdk_only=True)[0]['ok'])

    def test_version_parser_rejects_failed_process(self):
        with patch.object(doctor.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, '', 'javac 21')):
            self.assertIsNone(doctor.java_major('/bin/sh'))
        with patch.object(doctor.subprocess, 'run', side_effect=subprocess.TimeoutExpired('java', 10)):
            self.assertIsNone(doctor.java_major('/bin/sh'))

    def test_sdk_conflict_and_incomplete_build_tools_fail(self):
        sdk = self.root / 'sdk'
        (sdk / 'platforms/android-36').mkdir(parents=True)
        (sdk / 'platforms/android-36/android.jar').touch()
        (sdk / 'build-tools/36.0.0').mkdir(parents=True)
        with patch.object(doctor, 'java_major', return_value=21):
            rows = {r['check']: r['ok'] for r in doctor.inspect({'ANDROID_HOME': str(sdk), 'ANDROID_SDK_ROOT': '/other'}, self.root)}
        self.assertFalse(rows['SDK variables'])
        self.assertTrue(rows['Platform'])
        self.assertFalse(rows['Build tools'])

    def test_complete_sdk_and_wrapper_pass(self):
        sdk = self.root / 'sdk'
        for relative in ['platforms/android-36/android.jar', 'build-tools/36.0.0/aapt2']:
            path = sdk / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            path.chmod(0o755)
        for relative in ['gradlew', 'gradlew.bat', 'gradle/wrapper/gradle-wrapper.jar', 'gradle/wrapper/gradle-wrapper.properties']:
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            path.chmod(0o755)
        with patch.object(doctor, 'java_major', return_value=21), patch.object(doctor.shutil, 'which', return_value='/bin/sh'):
            self.assertTrue(all(r['ok'] for r in doctor.inspect({'ANDROID_HOME': str(sdk)}, self.root)))

    def test_setup_help_and_invalid_option_do_not_create_sdk(self):
        env = dict(os.environ, ANDROID_HOME=str(self.root / 'unused-sdk'))
        for arg, expected in [('--help', 0), ('--unknown-option', 2)]:
            result = subprocess.run(['bash', str(ROOT / 'scripts/setup-linux.sh'), arg], env=env,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, expected, result.stderr)
        self.assertFalse((self.root / 'unused-sdk').exists())

    def test_provisioning_with_fake_tools_installs_pinned_packages(self):
        # Exercise actual shell routing/quoting without downloading or accepting licenses.
        sdk = self.root / 'sdk with spaces'
        manager = sdk / 'cmdline-tools/latest/bin/sdkmanager'
        manager.parent.mkdir(parents=True)
        log = self.root / 'calls.jsonl'
        manager.write_text('#!/usr/bin/env python3\nimport json,os,sys\nwith open(os.environ["NATEORBIT_TEST_CALLS"],"a") as f: f.write(json.dumps(sys.argv[1:])+"\\n")\n')
        manager.chmod(0o755)
        jdk = self.root / 'jdk/bin'
        jdk.mkdir(parents=True)
        for tool in ['java', 'javac']:
            executable = jdk / tool
            executable.write_text('#!/bin/sh\necho \'openjdk version "21.0.1"\' >&2\n')
            executable.chmod(0o755)
        env = dict(os.environ, JAVA_HOME=str(jdk.parent), ANDROID_HOME=str(sdk),
                   ANDROID_SDK_ROOT=str(sdk), NATEORBIT_TEST_CALLS=str(log))
        result = subprocess.run(['bash', str(ROOT / 'scripts/setup-linux.sh'), '--install-sdk'],
                                env=env, capture_output=True, text=True, timeout=15)
        # Fake installer deliberately creates no SDK packages: final doctor must fail.
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        calls = [json.loads(line) for line in log.read_text().splitlines()]
        self.assertEqual(calls, [[f'--sdk_root={sdk}', '--licenses'],
                                [f'--sdk_root={sdk}', 'platform-tools', 'platforms;android-36', 'build-tools;36.0.0']])


if __name__ == '__main__':
    unittest.main()
