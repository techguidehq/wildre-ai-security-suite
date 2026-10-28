# Ghidra: Safe Reverse-Engineering Notes

Ghidra is a separate reverse-engineering application maintained by the NSA. Download it only from the official project and read current release prerequisites: https://github.com/NationalSecurityAgency/ghidra

## Prepare a safe lab
- Use a disposable VM or dedicated lab machine for untrusted artifacts.
- Take a snapshot; disable shared folders/clipboard and networking unless your authorized lab plan needs them.
- Do not use personal accounts, production credentials, or private files in the lab.
- Do not execute a sample just to observe behavior.

## Record evidence first
```bash
sha256sum ./authorized-sample
file ./authorized-sample
stat ./authorized-sample
```
Preserve the original; import a copy. Record provenance, authorization, hash, size, and date.

## Create a project
1. Launch Ghidra using its official install guide.
2. Select **File → New Project → Non-Shared Project**.
3. Use a neutral case ID that does not expose confidential names.
4. Select **File → Import File** and choose the authorized copy.
5. Check detected file format and architecture. Pause if unexpected.
6. Open the item in **CodeBrowser**.
7. Start **Auto Analysis** with default analyzers initially; record custom settings.
8. Save the project and keep analyst notes separately.

## Navigate
- **Listing:** assembly and addresses.
- **Decompiler:** C-like approximation, not original source; may be misleading.
- **Symbol Tree:** functions, labels, imports, exports.
- **Defined Strings:** clues, not proof.
- **Function Graph:** control flow.
- **Search:** string and memory searches.
Rename functions or add comments only when evidence supports the interpretation.

## Questions for the report
- What file format and architecture were detected?
- What are the entry point and important imports?
- Are there readable strings, URLs, paths, or configuration-like values?
- Which functions appear to parse input, access files, use networking, or launch processes?
- What evidence supports each hypothesis, and what benign explanation could fit?
- What did static analysis not establish?

## Report template
Scope/authorization; provenance; SHA-256 and size; file format/architecture; Ghidra version/settings; observations with addresses; hypotheses and confidence; limitations; next steps.

Never publish confidential binaries or screenshots containing private data. Dynamic analysis requires a separately approved isolated sandbox.
