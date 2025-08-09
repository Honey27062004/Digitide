import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

# Your OpenRouter API key (replace here)
OPENROUTER_API_KEY = "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"

# Sample company policy
policy_doc = """
Refund Policy:
We offer a full refund within 30 days of purchase if you are not satisfied with the product.
To request a refund, please contact customer support with your order details.
Refunds will be processed within 7 business days.
Products must be returned in original condition.
"""

chunks = [chunk.strip() for chunk in policy_doc.strip().split('\n') if chunk]

embedder = SentenceTransformer('all-MiniLM-L6-v2')
chunk_embeddings = embedder.encode(chunks)
dimension = chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(chunk_embeddings))

st.title("Company Policy Q&A with OpenRouter API")

question = st.text_input("Ask a question about our company policy or anything else:")

def query_openrouter_api(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 150,
        "top_p": 0.9
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

if question:
    keywords = ["refund", "policy", "return", "customer support"]
    if any(word in question.lower() for word in keywords):
        q_emb = embedder.encode([question])
        distances, indices = index.search(np.array(q_emb), 1)
        context = chunks[indices[0][0]]
        prompt = (
            f"Use the following policy excerpt to answer the question.\n\n"
            f"Policy excerpt:\n{context}\n\n"
            f"Question: {question}\nAnswer:"
        )
    else:
        prompt = question

    try:
        answer = query_openrouter_api(prompt)
    except Exception as e:
        answer = f"Error querying OpenRouter API: {e}"

    st.subheader("Answer:")
    st.write(answer)
