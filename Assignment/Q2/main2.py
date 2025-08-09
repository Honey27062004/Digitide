from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", pad_token_id=50256)

prompt = "Write a short poem about the ocean and its people:\n"

result = generator(
    prompt,
    max_new_tokens=80,
    temperature=0.8,
    top_p=0.95,
    repetition_penalty=1.1,
    num_return_sequences=1
)

print(result[0]["generated_text"])
