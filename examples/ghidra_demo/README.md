# Safe Ghidra demonstration

This folder contains a tiny, benign C program for practicing Ghidra navigation. It prints a message and calculates a checksum over a fixed string. It does not access the network, files, credentials, or system settings.

## Build on Kali Linux
```bash
sudo apt update
sudo apt install -y build-essential
gcc -O0 -g -fno-inline -o demo_app demo_app.c
sha256sum demo_app
file demo_app
strings -a demo_app | head -40
```
Only analyze the binary you built yourself. Import `demo_app` into a new non-shared Ghidra project and run Auto Analysis.

## Suggested exercise
1. Find `main` in Symbol Tree.
2. Inspect the Listing and Decompiler side by side.
3. Find the `WILDRE_DEMO_MARKER` string.
4. Identify the function that calculates the checksum.
5. Compare source names with decompiled function names.
6. Write down one fact, one hypothesis, and one limitation.
7. Record the SHA-256 and Ghidra version in your report.

Delete generated `demo_app` after the exercise if you do not need it; it is intentionally not committed.
