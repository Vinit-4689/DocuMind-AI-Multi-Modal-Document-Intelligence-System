from transformers import pipeline

# Load once
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_length=512
)


def generate_answer(query, context):
    prompt = f"""
    Answer the question based only on the context.

    Context:
    {context}

    Question:
    {query}
    """

    response = generator(prompt)[0]['generated_text']
    return response
