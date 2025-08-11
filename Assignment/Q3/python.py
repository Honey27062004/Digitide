from transformers import pipeline
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Your sample company policy text 
policy_doc = """
Refund Policy:
We offer a full refund within 30 days of purchase if you are not satisfied with the product.
To request a refund, please contact customer support with your order details.
Refunds will be processed within 7 business days.
Products must be returned in original condition.
"""

# 2. Split into chunks 
chunks = [chunk.strip() for chunk in policy_doc.strip().split('\n') if chunk]

# 3. Load sentence embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# 4. Embed chunks
chunk_embeddings = embedder.encode(chunks)

# 5. Build FAISS index
dimension = chunk_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(chunk_embeddings))

# 6. Define the question
question = "What is the refund policy?"

# 7. Embed the question
question_embedding = embedder.encode([question])

# 8. Search the index for the most relevant chunk(s)
k = 1  # top 1 chunk
distances, indices = index.search(np.array(question_embedding), k)

# 9. Retrieve the chunk text
relevant_chunk = chunks[indices[0][0]]

# 10. Use a text generation model to answer based on the retrieved chunk
generator = pipeline("text-generation", model="gpt2", pad_token_id=50256)

prompt = f"Answer the question based on the policy:\nPolicy excerpt: {relevant_chunk}\nQuestion: {question}\nAnswer:"

result = generator(
    prompt,
    max_new_tokens=50,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
    num_return_sequences=1
)

print(result[0]["generated_text"])

