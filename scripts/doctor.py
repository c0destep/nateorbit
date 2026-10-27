#!/usr/bin/env python3
"""Read-only JDK/SDK checks. No downloads, device access or secret inspection."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def java_major(executable):
    if not executable or not Path(executable).is_file():
        return None
    try:
        result = subprocess.run([str(executable), '-version'], capture_output=True,
                                text=True, timeout=10, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    match = re.search(r'(?:version\s+"|javac\s+)(\d+)', result.stdout + result.stderr)
    return int(match.group(1)) if result.returncode == 0 and match else None


def sdk_location(environ, root):
    for key in ('ANDROID_HOME', 'ANDROID_SDK_ROOT'):
        if environ.get(key):
            return Path(environ[key]).expanduser()
    props = root / 'local.properties'
    if props.is_file():
        match = re.search(r'^\s*sdk\.dir\s*[=:]\s*(.+)$', props.read_text(), re.M)
        if match:
            # Java properties escape spaces, backslashes, colons and equals signs.
            return Path(re.sub(r'\\([\\ :=])', r'\1', match.group(1).strip())).expanduser()
    return None


def inspect(environ=None, root=ROOT, jdk_only=False):
    environ = os.environ if environ is None else environ
    config = json.loads((root / 'scripts/android-env.json').read_text())
    rows = []

    def record(label, ok, detail):
        rows.append({'check': label, 'ok': bool(ok), 'detail': detail})

    java_home = environ.get('JAVA_HOME')
    java = Path(java_home) / 'bin/java' if java_home else shutil.which('java')
    javac = Path(java_home) / 'bin/javac' if java_home else shutil.which('javac')
    required = config['jdk']
    record('JDK', java_major(java) == required and java_major(javac) == required,
           f'JAVA_HOME / java e javac precisam de JDK {required}')
    if jdk_only:
        return rows
    sdk = sdk_location(environ, root)
    legacy_sdk = environ.get('ANDROID_SDK_ROOT')
    if environ.get('ANDROID_HOME') and legacy_sdk:
        record('SDK variables', Path(environ['ANDROID_HOME']).expanduser().resolve()
               == Path(legacy_sdk).expanduser().resolve(),
               'ANDROID_HOME e ANDROID_SDK_ROOT devem apontar para o mesmo SDK')
    record('Android SDK', sdk and sdk.is_dir(), 'ANDROID_HOME ou sdk.dir em local.properties')
    if sdk:
        api = config['compile_sdk']
        tools = config['build_tools']
        record('Platform', (sdk / f'platforms/android-{api}/android.jar').is_file(),
               f'Instalar platforms;android-{api}')
        aapt = sdk / f'build-tools/{tools}/aapt2'
        record('Build tools', aapt.is_file() and os.access(aapt, os.X_OK),
               f'Instalar build-tools;{tools} completo e executável')
    record('Git', shutil.which('git'), 'Git disponível no PATH')
    files = ['gradlew', 'gradlew.bat', 'gradle/wrapper/gradle-wrapper.jar',
             'gradle/wrapper/gradle-wrapper.properties']
    record('Wrapper', all((root / f).is_file() for f in files), 'Usar o Gradle wrapper do projeto')
    record('Wrapper executable', os.access(root / 'gradlew', os.X_OK), 'chmod +x gradlew no Linux')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jdk-only', action='store_true', help='Check just java/javac before SDK setup')
    parser.add_argument('--json', action='store_true', help='Machine-readable result')
    args = parser.parse_args()
    rows = inspect(jdk_only=args.jdk_only)
    ok = all(row['ok'] for row in rows)
    if args.json:
        print(json.dumps({'ok': ok, 'checks': rows}, ensure_ascii=False))
    else:
        for row in rows:
            print(f"{'OK' if row['ok'] else 'MISSING'}: {row['check']} — {row['detail']}")
        print('RESULT: ' + ('pré-requisitos encontrados; execute o build' if ok else
                            'pré-requisitos incompletos; veja docs/development/LINUX.md'))
        print('Este diagnóstico não valida downloads, licenças, compilação ou dispositivos.')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
