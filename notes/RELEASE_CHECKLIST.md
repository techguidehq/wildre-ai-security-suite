# Release checklist

- [ ] Run unit tests and all CLI smoke commands.
- [ ] Review `git diff` and `git status`.
- [ ] Confirm no `.env`, API keys, private logs, binaries, or credentials are staged.
- [ ] Review generated YARA output and clearly label it unvalidated.
- [ ] Test MCP using the chosen client; document exact SDK/client versions.
- [ ] Build the benign Ghidra demo locally and record its SHA-256.
- [ ] Verify GitHub Actions completes on Python 3.10, 3.11, and 3.12.
- [ ] Create a tagged release after CI is green.
