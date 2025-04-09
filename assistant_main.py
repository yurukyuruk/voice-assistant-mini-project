from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json
import ollama
import pyttsx3

# Load Vosk model
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Setup audio stream
q = queue.Queue()

def audio_callback(indata, frames, time, status):
    q.put(bytes(indata))

# Initialize TTS engine
tts = pyttsx3.init()
tts.setProperty('rate', 160)

# Function to get response from AI
def get_ai_response(text):
    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": text}]
    )
    return response['message']['content']

# Function to speak text
def speak(text):
    print("Assistant:", text)
    tts.say(text)
    tts.runAndWait()

# Main interaction loop
def run_voice_assistant():
    print("Voice Assistant Ready (speak to start)...")
    stream = sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=audio_callback)

    with stream:
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                user_text = result.get("text", "")

                if user_text:
                    print("You said:", user_text)

                    if user_text.lower() in ["exit", "quit", "stop"]:
                        speak("Okay, goodbye!")
                        break

                    stream.stop()

                    # Check if input is just a greeting or polite phrase
                    if any(phrase in user_text.lower() for phrase in [
                        "hello", "hi", "thank you", "thanks", "have a nice day"
                    ]):
                        ai_response = get_ai_response(user_text)
                        speak(ai_response)
                    else:
                        speak("Let me think about that...")
                        try:
                            ai_response = get_ai_response(user_text)
                            speak(ai_response)
                        except Exception as e:
                            print("Error:", e)
                            speak("Sorry, something went wrong.")

                    # Resume stream and optionally say "I'm listening..." for follow-ups
                    if not any(phrase in user_text.lower() for phrase in [
                        "exit", "quit", "stop", "thank you", "thanks", "have a nice day"
                    ]):
                        speak("I'm listening...")

                    stream.start()



# Run it!
if __name__ == "__main__":
    run_voice_assistant()
