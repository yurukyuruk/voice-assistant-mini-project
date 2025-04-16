import ollama

def test_system_prompt(system_prompt, user_input):
    response = ollama.chat(
        model='mistral',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    print(f"\nSystem Prompt: {system_prompt}")
    print(f"User Prompt: {user_input}")
    print(f"Assistant Response: {response['message']['content']}\n")


# Try different system prompts
if __name__ == "__main__":
    user_query = "Tell me a joke"

    # Prompt 1: Default neutral
    test_system_prompt(
        "You are a helpful, friendly voice assistant. Keep responses brief and clear.",
        user_query
    )

    # Prompt 2: Humorous style
    test_system_prompt(
        "You are a witty and humorous assistant. Add a playful tone to your responses.",
        user_query
    )

    # Prompt 3: Formal style
    test_system_prompt(
        "You are a polite, professional assistant. Speak formally and respectfully.",
        user_query
    )
