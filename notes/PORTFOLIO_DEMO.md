# Portfolio Demo Script (5–7 minutes)

1. Introduce the repository as an offline-first defensive toolkit.
2. Run `python -m unittest discover -s tests -v`.
3. Show `python -m wildre.cli summary examples/sample.log`.
4. Show `python -m wildre.cli iocs examples/sample.log --json`.
5. Show `python -m wildre.cli hash examples/sample.log`.
6. Show `python -m wildre.cli yara-draft examples/suspicious_strings.txt --name DemoRule`.
7. Explain the optional MCP server and its narrow tools.
8. Show the Ghidra notes and isolation requirements.

Be honest: IOC detection is pattern-based; severity counting is heuristic; YARA output is unvalidated; MCP needs an installed SDK and compatible client; no malware execution or live threat-intelligence lookup is included.
