from sentence_transformers import SentenceTransformer, util

# Golden standard responses
golden_responses = {
    "what's the weather like": "I would check the weather, but I don’t have that feature yet.",
    "remind me to drink water": "Got it! I’ll remind you to drink water regularly.",
    "let's stretch": "Stand up and roll your shoulders.",
    "quiz me on vocabulary": "The word is curious. It means: eager to know or learn something.",
    "hello": "Hello! How can I help you today?",
    "stop": "Goodbye!"
}

# Load the model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Semantic similarity scoring function
def assess_response(user_query, assistant_reply, golden_dataset):
    expected_reply = golden_dataset.get(user_query.lower())

    if expected_reply:
        embeddings = model.encode([assistant_reply, expected_reply], convert_to_tensor=True)
        similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
        print(f"Similarity Score: {similarity:.2f}")

        if similarity > 0.75:
            print("✅ Response quality is acceptable.")
        else:
            print("⚠️ Response needs improvement.")
    else:
        print("⚠️ No golden standard found for this query.")
