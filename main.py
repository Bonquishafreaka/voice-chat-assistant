from config import Config
from recorder import Recorder
from transcriber import Transcriber
from assistant import Assistant
from speaker import Speaker


def main():
    config = Config()
    config.validate()

    recorder = Recorder(config)
    transcriber = Transcriber(config)
    assistant = Assistant(config)
    speaker = Speaker()

    print("Voice chat ready. Say 'goodbye' to exit.\n")

    while True:
        audio = recorder.record()
        user_text = transcriber.transcribe(audio)

        if not user_text:
            print("(didn't catch that)\n")
            continue

        print(f"You: {user_text}")

        if any(word in user_text.lower() for word in ("goodbye", "exit", "quit")):
            speaker.speak("Goodbye!")
            break

        reply = assistant.reply(user_text)
        print(f"Assistant: {reply}\n")
        speaker.speak(reply)


if __name__ == "__main__":
    main()
