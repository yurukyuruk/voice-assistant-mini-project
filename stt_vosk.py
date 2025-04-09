import sounddevice as sd
import queue
import sys
import json
from vosk import Model, KaldiRecognizer


# Set up audio input stream
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print("Status:", status, file=sys.stderr)
    q.put(bytes(indata))

# Load the Vosk model
model_path = "vosk-model-small-en-us-0.15"
try:
    model = Model(model_path)
except Exception as e:
    sys.exit(1)

recognizer = KaldiRecognizer(model, 16000)

# Start audio stream
try:
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Say something... Press Ctrl+C to stop.")
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print("You said:", result.get("text", ""))
except KeyboardInterrupt:
    print("\n Voice assistant stopped by user.")

