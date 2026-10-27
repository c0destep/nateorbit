#!/usr/bin/env python3
"""Offline checks for repository skills, links and environment pin consistency."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    config = json.loads((ROOT / 'scripts/android-env.json').read_text())
    app = (ROOT / 'app/build.gradle.kts').read_text()
    assert re.search(rf'compileSdk\s*=\s*{config["compile_sdk"]}\b', app), 'compileSdk drift'
    assert f'kotlin.jvmToolchain({config["jdk"]})' in app, 'JDK drift'
    assert config['sdk_packages'] == ['platform-tools', f'platforms;android-{config["compile_sdk"]}',
                                     f'build-tools;{config["build_tools"]}'], 'SDK package drift'
    ci = (ROOT / '.github/workflows/android-checks.yml').read_text()
    assert 'bash scripts/check.sh' in ci, 'CI must run the local check entrypoint'
    assert f"java-version: '{config['jdk']}'" in ci, 'CI JDK drift'
    assert all(package in ci for package in config['sdk_packages']), 'CI SDK drift'
    skills = sorted((ROOT / '.agents/skills').glob('*/SKILL.md'))
    assert skills, 'No repository skills'
    names = set()
    for skill in skills:
        content = skill.read_text()
        assert content.startswith('---\n'), f'Missing frontmatter: {skill}'
        header, body = content[4:].split('\n---\n', 1)
        fields = dict(line.split(':', 1) for line in header.splitlines() if ':' in line)
        name = fields.get('name', '').strip()
        assert name == skill.parent.name and re.fullmatch(r'[a-z0-9-]{1,63}', name), skill
        assert name not in names, f'Duplicate skill: {name}'
        names.add(name)
        assert fields.get('description', '').strip() and body.strip(), skill
        assert not re.search(r'\bTODO\b|\[INSERT', content), f'Unfinished skill: {skill}'
        metadata = (skill.parent / 'agents/openai.yaml').read_text()
        assert f'${name}' in metadata, f'Metadata prompt missing invocation: {skill}'
    # Check actual Markdown file links, excluding external URLs and anchors.
    docs = [ROOT / 'README.md', ROOT / 'AGENTS.md', ROOT / 'docs/development/START-HERE.md',
            ROOT / 'docs/development/LINUX.md', ROOT / 'docs/development/CODEX.md']
    for document in docs:
        for target in re.findall(r'\[[^\]]+\]\(([^)\s]+)\)', document.read_text()):
            if '://' not in target and not target.startswith('#'):
                assert (document.parent / target.split('#')[0]).exists(), (document, target)
    print(f'PASS: {len(skills)} repository skills, documentation links and Android environment pins.')


if __name__ == '__main__':
    main()
