import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms.base import LLM
from pydantic import BaseModel, Field
import requests

# Your OpenRouter API key
OPENROUTER_API_KEY = "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"

# Custom LLM wrapper for OpenRouter
class OpenRouterLLM(LLM, BaseModel):
    api_key: str = Field(..., exclude=True)

    @property
    def _llm_type(self) -> str:
        return "openrouter"

    def _call(self, prompt: str, stop=None) -> str:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 150,
            "top_p": 0.9,
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        res_json = response.json()
        return res_json["choices"][0]["message"]["content"]

# Streamlit app starts here
st.title("Upload PDF and Ask Questions (OpenRouter LLM)")

# Upload PDF file
pdf_file = st.file_uploader("Upload company policy PDF", type=["pdf"])

if pdf_file is not None:
    # Extract text from PDF
    pdf_reader = PdfReader(pdf_file)
    full_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    # Split text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_text(full_text)

    # Create embeddings and FAISS vector store
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(docs, embedding_model)

    # Initialize OpenRouter LLM wrapper
    llm = OpenRouterLLM(api_key=OPENROUTER_API_KEY)

    # Create RetrievalQA pipeline
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

    # User input question
    question = st.text_input("Ask a question about the uploaded document:")

    if question:
        answer = qa.run(question)
        st.subheader("Answer:")
        st.write(answer)
