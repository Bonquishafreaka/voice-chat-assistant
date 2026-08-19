import whisper


class Transcriber:
    """Wraps Whisper for local speech-to-text."""

    def __init__(self, config):
        self.model = whisper.load_model(config.whisper_model)
        self.sr = config.sample_rate

    def transcribe(self, audio) -> str:
        result = self.model.transcribe(
            audio.astype("float32"), fp16=False, language="en"
        )
        return result["text"].strip()
