from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json
import ollama
import pyttsx3
import random

from intent_classifier import classify_intent
from assess_quality import assess_response, golden_responses  

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

# Stretching prompts
stretch_prompts = [
    "Stand up and roll your shoulders.",
    "Take a deep breath and stretch your arms above your head.",
    "Tilt your head gently from side to side.",
    "Stretch your back by leaning forward slowly.",
    "Rotate your ankles and wrists for a few seconds."
]

# Vocabulary list
vocab_list = [
    {"word": "resilient", "definition": "able to recover quickly from difficulties"},
    {"word": "gratitude", "definition": "the quality of being thankful"},
    {"word": "curious", "definition": "eager to know or learn something"},
    {"word": "observe", "definition": "to notice or perceive something"},
    {"word": "challenge", "definition": "a task that tests someone's abilities"}
]

# Function to get AI response (used for small talk)
def get_ai_response(prompt):
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                "role": "system",
                "content": "You are a helpful, friendly voice assistant that runs locally and supports wellness and learning tasks like reminders, stretching, and vocabulary training. Keep responses brief and clear."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
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
                    intent = classify_intent(user_text)

                    if intent == "get_weather":
                        reply = "I would check the weather, but I don’t have that feature yet."
                        speak(reply)

                    elif intent == "set_reminder":
                        reply = "Okay, what would you like to be reminded about?"
                        speak(reply)

                    elif intent == "start_stretch":
                        reply = random.choice(stretch_prompts)
                        speak(reply)

                    elif intent == "vocab_review":
                        word = random.choice(vocab_list)
                        reply = f"The word is {word['word']}. It means: {word['definition']}."
                        speak(reply)

                    elif intent == "small_talk":
                        reply = get_ai_response(user_text)
                        speak(reply)

                    elif intent == "exit":
                        speak("Goodbye!")
                        break

                    else:
                        reply = "Sorry, I didn't quite understand. Can you say that again?"
                        speak(reply)

                    # Run semantic similarity assessment if intent is known
                    if intent not in ["fallback", "exit"]:
                        assess_response(user_text, reply, golden_responses)

                    # Resume listening
                    if intent not in ["exit", "fallback"]:
                        speak("I'm listening...")
                    stream.start()

# Run it!
if __name__ == "__main__":
    run_voice_assistant()
