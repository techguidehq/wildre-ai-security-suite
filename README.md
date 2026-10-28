# WildRE AI Security Suite

Offline-first defensive cybersecurity portfolio: agent skills, Python triage tools, an optional MCP server, Kenya/Africa safety resources, Ghidra notes, and agent workflow templates.

## Requirements
Python 3.10+. CLI uses only the standard library.

## Install and test
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Commands
```bash
python -m wildre.cli summary examples/sample.log
python -m wildre.cli iocs examples/sample.log --json
python -m wildre.cli hash examples/sample.log
python -m wildre.cli yara-draft examples/suspicious_strings.txt --name ExampleRule
```

## Optional MCP server
```bash
python -m pip install -e ".[mcp]"
python -m wildre.mcp_server
```
See `integrations/mcp/README.md` and `notes/MCP_TESTING.md` for client setup and integration validation.

## Included
- `wildre/`: tested Python core, CLI, optional MCP server
- `skills/`: reverse engineering, malware triage, binary analysis
- `notes/`: full notes pack, Ghidra workflow, portfolio demo, roadmap
- `africa-cyber/`: mobile-money safety education starter
- `templates/`: Claude Code, Cursor, general agent task template
- `tests/`: automated tests
- `.github/workflows/tests.yml`: CI on Python 3.10–3.12
- `examples/ghidra_demo/`: benign C program for a hands-on Ghidra exercise
- `examples/`: synthetic data only

## Safety
Only analyze authorized systems and data. No sample execution, exploitation, arbitrary shell execution, automatic URL visits, or uploads. IOCs are candidates, not verdicts. YARA output is a draft and must be reviewed and tested. Ghidra is installed separately; follow its official current instructions.

Release checklist: `notes/RELEASE_CHECKLIST.md`. License: MIT.
