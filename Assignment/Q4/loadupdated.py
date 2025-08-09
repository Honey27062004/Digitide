import streamlit as st
import pandas as pd
import docx
import PyPDF2
import os
import io
import requests

# -----------------------
# CONFIG
# -----------------------
GROQ_API_KEY = "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"  # Replace with your actual key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="Multi-File Q&A", layout="centered")
st.title("📄 Multi-File Upload & Q&A App")

# -----------------------
# File Processing Functions
# -----------------------
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def read_txt(file):
    return file.read().decode("utf-8")

def read_csv(file):
    df = pd.read_csv(file)
    return df.to_string()

# -----------------------
# File Upload
# -----------------------
uploaded_files = st.file_uploader(
    "Upload PDF, TXT, DOCX, or CSV files", 
    type=["pdf", "txt", "docx", "csv"], 
    accept_multiple_files=True
)

all_text = ""

if uploaded_files:
    for file in uploaded_files:
        if file.name.endswith(".pdf"):
            all_text += read_pdf(file)
        elif file.name.endswith(".docx"):
            all_text += read_docx(file)
        elif file.name.endswith(".txt"):
            all_text += read_txt(file)
        elif file.name.endswith(".csv"):
            all_text += read_csv(file)
    st.success("✅ Files processed successfully!")

# -----------------------
# Q&A Section
# -----------------------
if all_text:
    question = st.text_input("Ask a question about the uploaded files:")

    if question:
        with st.spinner("Thinking..."):
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant that answers questions based on the given text."},
                    {"role": "user", "content": f"Context: {all_text}\n\nQuestion: {question}"}
                ],
                "temperature": 0.2
            }

            response = requests.post(GROQ_API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                answer = response.json()["choices"][0]["message"]["content"]
                st.markdown(f"**Answer:** {answer}")
            else:
                st.error(f"API Error: {response.text}")
