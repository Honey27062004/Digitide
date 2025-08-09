from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GROQ_API_KEY = "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"  # Replace with your real key

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_input = request.form["prompt"]

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama3-70b-8192",  # or any model Groq supports
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
        else:
            answer = f"Error: {response.status_code} - {response.text}"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
