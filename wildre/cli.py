import argparse, hashlib, json, sys
from pathlib import Path
from .core import summarize_log, extract_iocs, draft_yara_rule

def main(argv=None):
    p = argparse.ArgumentParser(prog="wildre", description="Offline defensive analysis helpers")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, helptext in [("summary", "Summarize a text log"), ("iocs", "Extract candidate indicators")]:
        sp = sub.add_parser(name, help=helptext); sp.add_argument("file", type=Path); sp.add_argument("--json", action="store_true")
    sp = sub.add_parser("hash", help="SHA-256 of raw file bytes"); sp.add_argument("file", type=Path)
    sp = sub.add_parser("yara-draft", help="Draft YARA from one string per line"); sp.add_argument("file", type=Path); sp.add_argument("--name", default="WildRE_Starter_Rule")
    a = p.parse_args(argv)
    try:
        if a.cmd == "hash":
            raw = a.file.read_bytes()
            print(json.dumps({"file": str(a.file), "algorithm": "sha256", "hex": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}, indent=2))
            return 0
        text = a.file.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise SystemExit(f"wildre: cannot read file: {exc}") from exc
    if a.cmd == "summary":
        result = summarize_log(text)
        if a.json: print(json.dumps(result, indent=2))
        else:
            print(f"File: {a.file}\nTotal lines: {result['total_lines']}\nBlank lines: {result['blank_lines']}\nLevel counts:")
            for k, v in result["level_counts"].items(): print(f"  {k}: {v}")
            print(f"First timestamp: {result['first_timestamp_seen'] or 'not detected'}")
            print(f"Last timestamp: {result['last_timestamp_seen'] or 'not detected'}")
            print("Note:", result["limitation"])
    elif a.cmd == "iocs":
        result = extract_iocs(text)
        if a.json: print(json.dumps(result, indent=2))
        else:
            for key in ("urls", "domains", "ipv4", "hashes"):
                print(key.upper() + ":")
                for item in result[key]: print("  " + item)
                if not result[key]: print("  (none)")
            print("\nNOTE:", result["warning"])
    else:
        try: print(draft_yara_rule(text.splitlines(), a.name))
        except ValueError as exc: raise SystemExit(f"wildre: {exc}") from exc
    return 0

if __name__ == "__main__": sys.exit(main())
