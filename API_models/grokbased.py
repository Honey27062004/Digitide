import openai

# Set your OpenAI API Key
openai.api_key = "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"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use "gpt-3.5-turbo" if not on GPT-4
        messages=[
            {"role": "system", "content": "You are a witty, cinematic assistant like Grok who replies with dramatic flair and humor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

# Example prompt
if __name__ == "__main__":
    prompt = input("🎬 Enter your hospital movie scene idea: ")
    reply = generate_response(prompt)
    print("\n🎥 Grok-like Output:\n", reply)
