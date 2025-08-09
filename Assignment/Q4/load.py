import streamlit as st
from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.title("Upload a file and split into chunks")

uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_uploaded_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    file_path = "temp_uploaded_file"

    if uploaded_file.name.endswith(".txt"):
        loader = TextLoader(file_path, encoding="utf-8")
    elif uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        st.error("Unsupported file type.")
        st.stop()

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    st.write(f"Total chunks created: {len(chunks)}")
