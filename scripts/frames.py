#!/usr/bin/env python3
"""
Extract a few evenly-spaced frames from a video so the agent can SEE the
speaker and write an ACCURATE identity anchor for the Seedance prompt.

The motion-hack prompt must keep the person recognizable in every beat (the
"identity anchor": their real traits -- hair, facial hair, headwear, glasses,
skin tone, clothing). To describe those faithfully instead of guessing, look
at a couple of real frames from the video first.

Usage:
    python frames.py <video> [count] [out_dir]

    count:   number of frames to extract, evenly spaced. Default 3.
    out_dir: where to write them. Default "frames".

Requires ffmpeg + ffprobe on PATH (already needed for transcription).
Writes frame_01.png ... frame_NN.png and prints their paths (one per line).
Everything runs locally: no API key, no account, no paid service.
"""
import sys
import os
import json
import subprocess


def duration_seconds(src):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", src],
        capture_output=True, text=True, check=True,
    )
    return float(json.loads(out.stdout)["format"]["duration"])


def main():
    if len(sys.argv) < 2:
        print("Usage: python frames.py <video> [count] [out_dir]")
        sys.exit(1)

    src = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "frames"
    os.makedirs(out_dir, exist_ok=True)

    dur = duration_seconds(src)
    paths = []
    # evenly spaced, skipping the very first/last instant (often black/blurred)
    for i in range(count):
        t = dur * (i + 1) / (count + 1)
        out = os.path.join(out_dir, f"frame_{i + 1:02d}.png")
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error",
             "-ss", f"{t:.3f}", "-i", src, "-frames:v", "1", out],
            check=True,
        )
        paths.append(out)

    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
