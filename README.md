# Motion Hack

Turn a short talking-head video into an animated **motion-graphics reel** prompt for **Seedance 2.0**.

The speaker is re-rendered in a stylized look that changes per beat, lip-synced to the original audio, with motion graphics that illustrate the words, animated transitions, animated cut-out text and timed SFX. Cut-paper collage is the flagship style, but any look works. The prompt is generated in **English and Chinese**, and you upload **only your video** to Seedance.

## How it works
1. Drop your video (and optionally a few collage style reference images) in a folder.
2. The skill runs a **preflight check** (`scripts/check_env.py`) and, if anything is missing, explains what it is for and asks permission to install it — so it's plug-and-play.
3. It transcribes your video **word-level** (Whisper, runs locally) to get exact timing.
4. It grabs a couple of **frames** so the stylized look stays the same recognizable you in every beat (the identity anchor).
5. It maps your words to collage styles, motion graphics, transitions, text and SFX.
6. It outputs a ready-to-paste Seedance 2.0 prompt in English and Chinese.

## Setup (free and local, no API keys)
The skill checks this for you: `scripts/check_env.py` reports what's missing, what each piece is for, and the install command for your OS — then asks before installing anything. To set it up manually:
- Install **Python 3.8+**.
- Install **ffmpeg** (includes `ffprobe`):
  - macOS: `brew install ffmpeg`
  - Windows: `winget install Gyan.FFmpeg` (or `choco install ffmpeg`)
  - Linux: `sudo apt install ffmpeg`
- Install the Python dependency: `pip install -r requirements.txt`

The first transcription downloads a Whisper model (~140MB) once. Everything else is local: no API key, no account, no paid service. Whisper is multilingual, so it works for any creator's language.

## Use it
This is a **Claude Code skill**. With the skill installed, give your agent your video (and optional style references) and ask it to make the collage reel prompt.

You can also run the transcriber directly:

```bash
python scripts/transcribe.py your-video.mp4 base transcript.json
```

## Files
- `SKILL.md` — the skill (workflow + the non-negotiable prompt rules).
- `references/prompt-template.md` — the full bilingual prompt skeleton, motion-graphic idea library, and a worked example.
- `references/style-library.md` — a menu of proven collage / motion-graphics styles to assign per beat.
- `scripts/check_env.py` — preflight dependency check (reports what's missing and how to install it).
- `scripts/transcribe.py` — local word-level transcription (Whisper).
- `scripts/frames.py` — extracts identity-anchor frames so the face stays the same person across beats.

## License
MIT. See `LICENSE`.
