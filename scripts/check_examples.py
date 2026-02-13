#!/usr/bin/env python3
import sys
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
RUN = [sys.executable, str(ROOT / "scripts" / "run_webppl.py")]

def iter_examples():
    for p in (ROOT / "examples").rglob("*.wppl"):
        yield p

def main():
    failed = 0
    for ex in sorted(iter_examples()):
        cmd = RUN + [str(ex), "--random-seed", "0"]
        proc = subprocess.run(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if proc.returncode != 0:
            failed += 1
            print("="*80)
            print("FAILED:", ex)
            print(proc.stdout)
    if failed:
        print(f"{failed} example(s) failed.")
        return 1
    print("All examples ran successfully.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
