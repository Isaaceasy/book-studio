#!/usr/bin/env python3
"""Find git (including the copy bundled with GitHub Desktop) and commit a stage.

Usage:
  python scripts/git_helper.py find
  python scripts/git_helper.py commit "Stage 3: architecture lock" [path ...]
  python scripts/git_helper.py status
Never pushes (the assistant has no credentials); prints whether the branch is ahead so the owner can push from their Git client.
Adds the standard Co-Authored-By trailer.
"""
import os
import shutil
import subprocess
import sys

TRAILER = "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"


def find_git():
    g = shutil.which("git")
    if g:
        return g
    base = os.path.join(os.environ.get("LOCALAPPDATA", ""), "GitHubDesktop")
    if os.path.isdir(base):
        for d in sorted(os.listdir(base), reverse=True):
            p = os.path.join(base, d, "resources", "app", "git", "cmd", "git.exe")
            if os.path.exists(p):
                return p
    return None


def run(g, *args):
    r = subprocess.run([g, *args], capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    g = find_git()
    if not g:
        sys.exit("git not found. Install Git or GitHub Desktop.")
    cmd = sys.argv[1] if len(sys.argv) > 1 else "find"
    if cmd == "find":
        print(g)
    elif cmd == "status":
        print(run(g, "status", "--short", "--branch")[1])
    elif cmd == "commit":
        msg = sys.argv[2]
        paths = sys.argv[3:] or ["."]
        run(g, "add", *paths)
        code, out = run(g, "commit", "-q", "-m", msg + "\n\n" + TRAILER)
        print(out or "committed")
        code, out = run(g, "status", "--short", "--branch")
        first = out.splitlines()[0] if out else ""
        print(first)
        if "ahead" in first:
            print("NOTE: commits are local. Push from your Git client so a cloud session can see them.")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
