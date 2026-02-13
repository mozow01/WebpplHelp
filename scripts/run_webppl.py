#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def find_webppl_executable(project_root: Path) -> str:
    # 1) Prefer local install (cross-platform)
    candidates = [
        project_root / "node_modules" / ".bin" / "webppl",
        project_root / "node_modules" / ".bin" / "webppl.cmd",
        project_root / "node_modules" / ".bin" / "webppl.ps1",
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    # 2) Fallback to PATH
    return "webppl"

def main(argv):
    if len(argv) < 2:
        print("Usage: run_webppl.py <file.wppl> [webppl args...]", file=sys.stderr)
        return 2

    project_root = Path(__file__).resolve().parents[1]
    exe = find_webppl_executable(project_root)

    wppl_file = argv[1]
    extra = argv[2:]

    # Ensure deterministic output unless caller overrides
    # (WebPPL supports --random-seed int; see CLI source.)
    cmd = [exe, wppl_file] + extra

    # If the executable is a .ps1 wrapper, we need to run through powershell.
    if exe.endswith(".ps1") and os.name == "nt":
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", exe, wppl_file] + extra

    proc = subprocess.run(cmd, cwd=str(project_root), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    sys.stdout.write(proc.stdout)
    return proc.returncode

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
