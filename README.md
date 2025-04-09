# Voice Assistant Mini Project

This is a simple offline AI voice assistant developed in Python. It listens to user speech, converts it into text using a local speech recognition model, generates a response using a local language model, and replies through text-to-speech. All major functionalities are performed locally without the need for an internet connection.

---

## Features

- Speech-to-text using Vosk
- Local AI-generated responses using Ollama (Mistral model)
- Text-to-speech with pyttsx3
- Integrated interaction loop (listen → process → speak)
- Spoken feedback messages to improve user experience

---

## Project Structure

```
voice_assistant_project/
│
├── assistant_main.py       # Main interaction loop
├── stt_vosk.py             # Voice input and speech-to-text (Vosk)
├── nlp_response.py         # AI response using Ollama
├── tts_engine.py           # Text-to-speech output
└── README.md               # Project documentation
```

*Note: Large model files (e.g., Vosk model) are not included in this repository.*

---

## Installation

### Requirements

- Python 3.10 or higher
- Install required libraries using pip:

```
pip install vosk pyttsx3 sounddevice ollama
```

---

## Setup Instructions

1. Clone this repository to your local machine.
2. Download the Vosk model (e.g., `vosk-model-small-en-us-0.15`) from the official Vosk website:  
   https://alphacephei.com/vosk/models  
   Extract the folder and place it in your project directory.
3. Install and start Ollama (https://ollama.com/) and pull a compatible language model such as Mistral:

```
ollama pull mistral
```

---

## Running the Assistant

Once everything is set up, run the assistant:

```
python assistant_main.py
```

The assistant will begin listening for voice input. Speak a command or question and receive a spoken response. Say "exit", "quit", or "stop" to end the session.

---

## Reflection

This project was developed as part of a human-AI collaboration mini project. The process involved combining separate modules for listening, understanding, and responding. Challenges included speech recognition errors, integration of components, and user experience design. The assistant was enhanced by adding auditory feedback to inform users of its status (e.g., listening, processing). Future improvements may include better speech accuracy, a graphical interface, and persistent memory features.

---

## Acknowledgements

- [Vosk Speech Recognition](https://github.com/alphacep/vosk-api)
- [Ollama Language Models](https://ollama.com/)
- [pyttsx3 Text-to-Speech](https://pypi.org/project/pyttsx3/)

---

## License

This project is provided for educational and personal use.
