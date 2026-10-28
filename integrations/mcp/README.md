# MCP Setup

Install optional dependency:
```bash
python -m pip install -e ".[mcp]"
python -m wildre.mcp_server
```
The stdio server may look idle when started alone; an MCP-compatible client normally launches it. Example config (replace paths with absolute paths and verify your client's config schema):
```json
{
  "mcpServers": {
    "wildre-defensive-toolkit": {
      "command": "/ABSOLUTE/PATH/.venv/bin/python",
      "args": ["-m", "wildre.mcp_server"],
      "cwd": "/ABSOLUTE/PATH"
    }
  }
}
```
Windows uses `.venv/Scripts/python.exe`. Do not store API keys in this config. Enable only servers you trust.

Tools: `summarize_log_text`, `extract_candidate_iocs`, `hash_supplied_text`, `draft_yara_rule_from_strings`. The server analyzes supplied text only; no arbitrary file reads, shell commands, sample execution, or network lookups.
