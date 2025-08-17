import streamlit as st
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def chat_with_llama(prompt, model="llama3.2"):
    """Send prompt to local Llama 3.2 model via Ollama API."""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

st.set_page_config(page_title="Local Llama 3.2 Chat", page_icon="🤖", layout="centered")
st.title("🤖Ollama Local Model(Llama 3.2)")

user_input = st.text_area("Type your message:", height=100)

if st.button("Send"):
    if user_input.strip():
        with st.spinner("Llama 3.2 is thinking..."):
            answer = chat_with_llama(user_input)
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**Llama 3.2:** {answer}")
    else:
        st.warning("Please enter a message.")
