# MCP integration testing

The core toolkit tests run without MCP dependencies. The optional MCP server needs a compatible MCP SDK/client.

## Local checks
```bash
python -m pip install -e "[mcp]"
python -m unittest discover -s tests -v
python -m wildre.mcp_server
```
The stdio server is intended to be launched by an MCP client; a terminal session that appears idle is not by itself a failure.

## Client-level validation checklist
- [ ] Client discovers `summarize_log_text`
- [ ] Client discovers `extract_candidate_iocs`
- [ ] Client discovers `hash_supplied_text`
- [ ] Client discovers `draft_yara_rule_from_strings`
- [ ] Sample text returns expected output
- [ ] Invalid/empty YARA strings return a clear error
- [ ] No tools can read arbitrary paths, execute shell commands, or make network requests
- [ ] Client logs contain no secrets or private sample data

The repository CI validates the core library and CLI. It does not claim a client-level MCP handshake has passed until the checklist is completed with the chosen client and SDK version.
