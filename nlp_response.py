import ollama

def get_response(prompt):
    """
    Sends a prompt to the local Ollama model and returns the assistant's response.
    """
    response = ollama.chat(
        model='mistral',  l
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']


# Example usage for testing the model
if __name__ == "__main__":
    print("Voice Assistant (powered by Ollama - mistral)")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Exiting. Bye!")
                break
            reply = get_response(user_input)
            print("Assistant:", reply)
        except KeyboardInterrupt:
            print("\nExiting. Bye!")
            break
