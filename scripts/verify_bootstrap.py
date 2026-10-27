#!/usr/bin/env python3
"""Offline integrity checks for the team handoff; not Android tests."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
backlog=json.loads((ROOT/'planning/backlog.json').read_text())['items']
graph={x['id']:x['dependencies'] for x in backlog}
assert len(graph)==len(backlog), "Duplicate backlog IDs"
finished=set()
def visit(k,chain):
    assert k in graph, f'Unknown dependency {k}'
    assert k not in chain, f'Dependency cycle at {k}'
    if k in finished:return
    for dep in graph[k]:visit(dep,chain|{k})
    finished.add(k)
for k in graph:visit(k,set())
for f in (ROOT/'app/src').rglob('*.xml'):ET.parse(f)
assert 'Apache License' in (ROOT/'LICENSE').read_text()
assert 'applicationId = "dev.nateorbit.app"' in (ROOT/'app/build.gradle.kts').read_text()
assert 'namespace = "cc.sovellus.vrcaa"' in (ROOT/'app/build.gradle.kts').read_text()
assert not (ROOT/'.github/workflows/nightly.yml').exists()
ci=(ROOT/'.github/workflows/android-checks.yml').read_text()
assert 'schedule:' not in ci and 'write-all' not in ci
for action in re.findall(r'uses:\s+([^\s]+)',ci):assert re.search(r'@[a-f0-9]{40}$',action),action
for f in ['AGENTS.md','CONTRIBUTING.md','docs/development/START-HERE.md','planning/sprint-01.md','UPSTREAM.md']:
    assert (ROOT/f).is_file(),f
print(f'PASS: {len(backlog)} backlog items, acyclic dependencies, XML, license, identity and CI policy.')
