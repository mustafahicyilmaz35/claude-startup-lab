"""Local package checks, not a replacement for claude plugin validate."""
from pathlib import Path
import json
import re
import sys
root = Path(__file__).resolve().parents[1]
errors = []
try:
    market = json.loads((root / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    assert market['name'] == 'startup-lab'
    assert market['owner']['name']
    assert len(market['plugins']) == 10
    names = set()
    for item in market['plugins']:
        name = item['name']
        assert re.fullmatch(r'[a-z0-9-]+', name), name
        assert name not in names, name
        names.add(name)
        path = (root / item['source']).resolve()
        assert path.is_relative_to(root), name
        manifest = json.loads((path / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        assert manifest['name'] == name
        assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
        command = (path / 'commands/run.md').read_text(encoding='utf-8')
        assert command.startswith('---\n')
        front = command.split('---', 2)[1]
        assert 'disable-model-invocation: true' in front
        assert 'description:' in front
        assert '$ARGUMENTS' in command
        assert len(command) > 1000
    for filename in ['README.md', 'docs/INSTALL.md', 'LICENSE']:
        assert (root / filename).is_file(), filename
except (AssertionError, KeyError, ValueError, OSError) as exc:
    errors.append(str(exc) or type(exc).__name__)
if errors:
    print('FAIL:', '; '.join(errors))
    sys.exit(1)
print('PASS: 10 manifests, marketplace, manual commands, arguments and docs')
