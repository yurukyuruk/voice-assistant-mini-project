import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)     # speed (default ~200)
    engine.setProperty('volume', 1.0)   # volume (0.0 to 1.0)

    print("Speaking...")
    engine.say(text)
    engine.runAndWait()

# Example use
if __name__ == "__main__":
    while True:
        user_input = input("Text to speak (or 'q' to quit): ")
        if user_input.lower() in ['q', 'quit', 'exit']:
            break
        speak_text(user_input)
