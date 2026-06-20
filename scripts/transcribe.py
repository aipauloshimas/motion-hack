#!/usr/bin/env python3
"""
Word-level transcription with OpenAI Whisper.

Outputs every spoken word with its exact start/end time, which is what the
collage-reel-prompt skill needs to land styles, text and motion graphics on the beat.

Usage:
    python transcribe.py <video_or_audio_file> [model] [out.json]

    model:  whisper model name. Default "base" (multilingual, ~140MB, good balance).
            Use "small" or "medium" for more accuracy, "tiny" for speed.
    out:    optional path to write the JSON. If omitted, prints to stdout.

Requires: openai-whisper (pip install -r requirements.txt) and ffmpeg on PATH.
The first run downloads the model once (needs internet). Everything runs locally,
no API key, no account, no paid service.
"""
import sys
import json


def main():
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <video_or_audio_file> [model] [out.json]")
        sys.exit(1)

    src = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "base"
    out_path = sys.argv[3] if len(sys.argv) > 3 else None

    import whisper  # imported here so --help style errors are fast
    model = whisper.load_model(model_name)
    result = model.transcribe(src, word_timestamps=True)

    words = []
    for seg in result.get("segments", []):
        for w in seg.get("words", []):
            words.append({
                "w": w["word"].strip(),
                "start": round(float(w["start"]), 3),
                "end": round(float(w["end"]), 3),
            })

    data = {
        "source": src,
        "language": result.get("language"),
        "text": result.get("text", "").strip(),
        "words": words,
    }
    payload = json.dumps(data, ensure_ascii=False, indent=2)

    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(payload)
        print(f"wrote {out_path} ({len(words)} words)")
    else:
        print(payload)


if __name__ == "__main__":
    main()
