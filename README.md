# Voice Chat Assistant

A local voice assistant: speak, get a spoken reply. Uses Whisper for
speech-to-text, Claude for the conversation, and Coqui TTS for speech
output. Conversation history is retained across turns.

## Architecture

```
Mic → Recorder → Whisper (STT) → Claude → Coqui (TTS) → Speaker
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # add your Anthropic API key
python main.py
```

## Features

- Automatic silence detection to end recording
- Fully local STT and TTS (only the LLM turn hits the network)
- Multi-turn conversation memory
- Configurable models, sample rate, and prompt via `config.py`

## Notes

First run downloads the Whisper and TTS model weights.
