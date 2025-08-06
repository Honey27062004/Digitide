from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load a Grok-style model — switch to gpt2-medium if no GPU
generator = pipeline(
    "text-generation",
    model="gpt2-medium"  # Replace with another if GPU available
)

@app.route('/', methods=['GET', 'POST'])
def home():
    generated_text = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        grok_prompt = f"🎬 Write a dramatic movie scene involving hospital management: {prompt}"
        output = generator(
            grok_prompt,
            max_length=300,
            temperature=0.9,
            repetition_penalty=1.2,
            do_sample=True,
            top_p=0.95,
            num_return_sequences=1
        )
        generated_text = output[0]['generated_text']
    return render_template('index.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
