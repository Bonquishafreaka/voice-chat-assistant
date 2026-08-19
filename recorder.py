import numpy as np
import sounddevice as sd


class Recorder:
    """Records from the mic until a period of silence is detected."""

    def __init__(self, config):
        self.sr = config.sample_rate
        self.channels = config.channels
        self.threshold = config.silence_threshold
        self.silence_duration = config.silence_duration

    def record(self) -> np.ndarray:
        print("Listening... (speak now)")
        frames = []
        silent_chunks = 0
        chunk_size = int(self.sr * 0.1)
        max_silent = int(self.silence_duration / 0.1)
        started = False

        with sd.InputStream(
            samplerate=self.sr, channels=self.channels, dtype="float32"
        ) as stream:
            while True:
                chunk, _ = stream.read(chunk_size)
                chunk = chunk.flatten()
                frames.append(chunk)

                amplitude = np.abs(chunk).mean()
                if amplitude > self.threshold:
                    started = True
                    silent_chunks = 0
                elif started:
                    silent_chunks += 1

                if started and silent_chunks > max_silent:
                    break

        audio = np.concatenate(frames)
        return audio
