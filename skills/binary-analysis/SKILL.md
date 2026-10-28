---
name: binary-analysis
description: Repeatable first-pass analysis of authorized binary artifacts.
---
# Binary Analysis
Confirm permission; preserve a read-only original; record SHA-256 and size; identify format/architecture; inspect headers, sections, imports/exports, symbols, and strings; note anomalies without inferring intent from one indicator; report evidence, uncertainty, and next steps. Suggested Linux tools: `sha256sum`, `file`, `strings`, `readelf`, `objdump`, and Ghidra. No target execution is required for initial static analysis.
