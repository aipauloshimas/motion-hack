#!/usr/bin/env python3
"""
Preflight environment check for the motion-hack skill.

Run this FIRST. It verifies everything the skill needs and, for anything
missing, explains what it is FOR and prints the exact install command for the
current operating system. It does NOT install anything itself -- it only
reports, so the agent can explain each item and ask the user for permission
before installing. That keeps the skill plug-and-play and safe.

Usage:
    python check_env.py

Exit code 0 if everything is present, 1 if something is missing.
Uses only the Python standard library, so it runs even before
openai-whisper is installed.
"""
import sys
import shutil
import platform
import importlib.util

OS = platform.system()  # 'Windows', 'Darwin' (macOS), or 'Linux'


def ffmpeg_install_cmd():
    if OS == "Windows":
        return "winget install Gyan.FFmpeg   (or: choco install ffmpeg)"
    if OS == "Darwin":
        return "brew install ffmpeg"
    return "sudo apt install ffmpeg   (Debian/Ubuntu; use your distro's package manager otherwise)"


def main():
    # (name, ok, what it is FOR, how to install)
    checks = []

    py_ok = sys.version_info >= (3, 8)
    checks.append((
        f"Python {sys.version_info.major}.{sys.version_info.minor}",
        py_ok,
        "runs the transcription and frame-extraction scripts",
        "install Python 3.8+ from https://python.org, then re-run this check",
    ))

    ff_ok = shutil.which("ffmpeg") is not None
    checks.append((
        "ffmpeg",
        ff_ok,
        "decodes the video's audio so Whisper can transcribe it",
        ffmpeg_install_cmd(),
    ))

    fp_ok = shutil.which("ffprobe") is not None
    checks.append((
        "ffprobe",
        fp_ok,
        "reads the video duration so frames.py can sample identity-anchor frames",
        ffmpeg_install_cmd() + "  (ffprobe ships with ffmpeg)",
    ))

    wh_ok = importlib.util.find_spec("whisper") is not None
    checks.append((
        "openai-whisper",
        wh_ok,
        "local, word-level transcription (a start/end time for every word)",
        "pip install -r requirements.txt   (or: pip install openai-whisper)",
    ))

    print("motion-hack environment check")
    print("-" * 30)
    missing = []
    for name, ok, what_for, fix in checks:
        print(f"[{'OK' if ok else 'MISSING'}] {name}  --  {what_for}")
        if not ok:
            missing.append((name, what_for, fix))

    if not missing:
        print("\nAll good. Everything the skill needs is installed.")
        return 0

    print("\n" + "=" * 30)
    print(f"{len(missing)} dependency(ies) missing. What each is for and how to install:\n")
    for name, what_for, fix in missing:
        print(f"- {name}: {what_for}")
        print(f"    install: {fix}\n")
    print("Explain each item to the user, ask permission, install, then re-run this check.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
