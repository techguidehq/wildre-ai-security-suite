"""Pure offline-first defensive analysis helpers."""
from collections import Counter
import hashlib
import re

LEVELS = ("critical", "alert", "emerg", "fatal", "error", "warning", "warn", "info", "debug")
TS = re.compile(r"\b(?:\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}|\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\b", re.I)
URL = re.compile(r"\bhttps?://[^\s\"'<>]+", re.I)
DOMAIN = re.compile(r"\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:com|net|org|io|co|ke|africa|info|biz|dev|app|xyz|online|site|cloud|edu|gov)\b", re.I)
IP = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
HASH = re.compile(r"\b(?:[a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64})\b", re.I)

def summarize_log(text):
    lines = text.splitlines()
    counts = Counter()
    for line in lines:
        low = line.lower()
        level = next((x for x in LEVELS if re.search(rf"\b{re.escape(x)}\b", low)), "unclassified")
        counts[level] += 1
    stamps = [m.group(0) for line in lines if (m := TS.search(line))]
    return {"total_lines": len(lines), "blank_lines": sum(not x.strip() for x in lines),
            "level_counts": dict(sorted(counts.items())),
            "first_timestamp_seen": stamps[0] if stamps else None,
            "last_timestamp_seen": stamps[-1] if stamps else None,
            "limitation": "Keyword-based summary only; not a full parser or incident verdict."}

def extract_iocs(text):
    return {"urls": sorted({x.rstrip(".,);]") for x in URL.findall(text)}),
            "domains": sorted({x.lower() for x in DOMAIN.findall(text)}),
            "ipv4": sorted(set(IP.findall(text))), "hashes": sorted(set(HASH.findall(text))),
            "warning": "Candidate indicators only. Validate context; do not visit or block automatically."}

def sha256_text(text):
    raw = text.encode("utf-8")
    return {"algorithm": "sha256", "hex": hashlib.sha256(raw).hexdigest(), "bytes_hashed": len(raw),
            "scope": "UTF-8 bytes of supplied text, not necessarily original file bytes."}

def _escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")

def _identifier(s):
    s = re.sub(r"\W+", "_", s)
    return "Rule_" + s if not s or s[0].isdigit() else s

def draft_yara_rule(strings, name="WildRE_Starter_Rule"):
    items = []
    for item in strings:
        item = item.strip()
        if item and item not in items:
            items.append(item)
    if not items:
        raise ValueError("Provide at least one non-empty string.")
    if len(items) > 50 or any(len(x) > 500 for x in items):
        raise ValueError("Maximum 50 strings; each must be 500 characters or fewer.")
    body = "\n".join(f'        $s{i} = "{_escape(s)}" ascii wide' for i, s in enumerate(items, 1))
    condition = "any of them" if len(items) > 1 else "$s1"
    return ('// DRAFT ONLY: review, test, and tune before operational use.\n'
            f'rule {_identifier(name)}\n{{\n    meta:\n'
            '        description = "Starter rule generated from analyst-provided strings"\n'
            '        status = "unvalidated"\n    strings:\n'
            f'{body}\n    condition:\n        {condition}\n}}\n')
