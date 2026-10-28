# WildRE Notes Pack

## Setup
```bash
python --version
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
```
Use `python3` instead of `python` if that is how Python is installed on your Linux system.

## Commands
- `python -m wildre.cli summary examples/sample.log` — heuristic severity-word and timestamp summary.
- `python -m wildre.cli iocs examples/sample.log --json` — candidate URLs, domains, IPv4 addresses, and hashes.
- `python -m wildre.cli hash examples/sample.log` — SHA-256 of raw file bytes.
- `python -m wildre.cli yara-draft examples/suspicious_strings.txt --name DemoRule` — prints a draft rule, not a scanner.

## MCP
Install with `python -m pip install -e ".[mcp]"`, then run `python -m wildre.mcp_server`. The process waits for a compatible MCP client; it may look idle when started by itself. It exposes only text-in/text-out tools, not arbitrary file reads, shell commands, sample execution, or internet access. See `integrations/mcp/README.md`.

## Ghidra
Ghidra is a separate application. Read `GHIDRA_GUIDE.md` for safe setup, project creation, auto-analysis, navigation, and report notes.

## AI skills/templates
`skills/` has reverse engineering, malware triage, and binary analysis playbooks. `templates/` has Claude Code, Cursor, and generic task instructions. Review them before copying into other projects.

## Troubleshooting
- `No module named wildre`: run from repository root or `python -m pip install -e .`.
- MCP import error: install the `mcp` optional extra.
- Empty IOC result: supported patterns are deliberately limited.
- YARA false positives: use more distinctive strings and test against known-clean files in an authorized lab.

## Privacy checklist
Never publish API keys, passwords, OTPs, private logs, customer records, private hostnames, or malware samples. Use synthetic examples for public demos.
