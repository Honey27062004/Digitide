import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def chat_with_llama(prompt, model="llama3.2"):
    """
    Send a prompt to the local Llama 3.2 model via Ollama API and return the response.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False 
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("🤖 Llama 3.2 Chat — type 'exit' to quit")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        answer = chat_with_llama(user_input)
        print(f"Llama 3.2: {answer}")
