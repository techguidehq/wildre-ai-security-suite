"""Optional MCP server: install the mcp extra before launching."""
import json
try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit('Install with: python -m pip install -e ".[mcp]"') from exc
from .core import summarize_log, extract_iocs, sha256_text, draft_yara_rule

mcp = FastMCP("WildRE Defensive Toolkit")

@mcp.tool()
def summarize_log_text(text: str) -> str:
    """Summarize supplied log text with keyword counts; no file or network access."""
    return json.dumps(summarize_log(text), indent=2)

@mcp.tool()
def extract_candidate_iocs(text: str) -> str:
    """Extract candidate URLs, domains, IPv4 addresses, and hashes from text."""
    return json.dumps(extract_iocs(text), indent=2)

@mcp.tool()
def hash_supplied_text(text: str) -> str:
    """SHA-256 hash of UTF-8 bytes of supplied text, not necessarily original file bytes."""
    return json.dumps(sha256_text(text), indent=2)

@mcp.tool()
def draft_yara_rule_from_strings(strings: list[str], name: str = "WildRE_Starter_Rule") -> str:
    """Draft a YARA rule from strings; does not validate or scan files."""
    try: return draft_yara_rule(strings, name)
    except ValueError as exc: return json.dumps({"error": str(exc)})

if __name__ == "__main__":
    mcp.run()
