---
name: defensive-reverse-engineering
description: Authorized, evidence-led static and dynamic review.
---
# Defensive Reverse Engineering
1. Confirm authorization, scope, owner, and handling restrictions.
2. Preserve original; work on a copy; record SHA-256 and size.
3. Identify format and architecture with trusted local tools.
4. Inspect metadata, imports, strings, sections, resources, signatures, and embedded paths.
5. Separate observations from hypotheses; include confidence and benign alternatives.
6. If approved, perform dynamic analysis only in a disposable isolated lab.
7. Report scope, tools, evidence, limitations, and next steps.
Never run unknown samples on a daily-use machine or upload confidential artifacts without approval.
