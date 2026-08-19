import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    model: str = "claude-sonnet-4-6"
    max_tokens: int = 1024
    sample_rate: int = 16000
    channels: int = 1
    silence_threshold: float = 0.01
    silence_duration: float = 1.5
    whisper_model: str = "base.en"
    system_prompt: str = (
        "You are a helpful voice assistant. Keep responses concise "
        "and conversational, since they will be spoken aloud."
    )

    def validate(self) -> None:
        if not self.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY is not set. Add it to your .env file.")
