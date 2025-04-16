import ollama

def classify_intent(prompt):
    intent_query = f"""
You are an intent classifier. Given the following user prompt, respond ONLY with the intent name from this list:

[intents: get_weather, set_reminder, start_stretch, vocab_review, small_talk, exit]

User Prompt: "{prompt}"

Only return the intent name. If the intent is unclear, respond with: fallback
"""
    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": intent_query}]
    )
    return response['message']['content'].strip().lower()
