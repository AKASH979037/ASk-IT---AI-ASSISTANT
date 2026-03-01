from app.services.embeddings import embed
from app.db.chroma import search_similar
from app.services.llm import generate_with_ollama

SIMILARITY_THRESHOLD = 0.6

def generate_answer(question: str):
    query_embedding = embed(question)
    results = search_similar(query_embedding)

    documents = results.get("documents", [[]])[0]
    if not documents:
        return "No relevant information found.", 0.0

    context = "\n\n".join(documents)

    prompt = f"""
    Answer only from the context below.
    If not found, say you don't know.

    Context:
    {context}

    Question:
    {question}
    """

    answer = generate_with_ollama(prompt)

    # Basic confidence logic (placeholder)
    confidence = 0.8 if len(documents) > 0 else 0.0

    return answer, confidence