import numpy as np
import sounddevice as sd
from TTS.api import TTS


class Speaker:
    """Local text-to-speech using Coqui TTS."""

    def __init__(self, model_name: str = "tts_models/en/ljspeech/tacotron2-DDC"):
        self.tts = TTS(model_name=model_name, progress_bar=False)
        self.sr = self.tts.synthesizer.output_sample_rate

    def speak(self, text: str) -> None:
        if not text:
            return
        wav = self.tts.tts(text=text)
        audio = np.array(wav, dtype="float32")
        sd.play(audio, self.sr)
        sd.wait()
