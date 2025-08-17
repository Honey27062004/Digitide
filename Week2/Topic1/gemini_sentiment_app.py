import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyA1Cyn9KNTuwX-6rrMiXqCMuT6h-Q1WmqM")

st.title("Zero-shot vs Few-shot Prompting - Sentiment Analysis ")

sentence = st.text_input("Enter a sentence to classify sentiment:")

mode = st.radio("Choose Prompting Mode:", ["Zero-shot", "Few-shot"])

if mode == "Zero-shot":
    prompt = f"Determine if the following sentence is positive or negative: \"{sentence}\""
else:
    prompt = (
        "Example 1: \"I am happy today.\" → Positive\n"
        "Example 2: \"I am sad today.\" → Negative\n"
        "Example 3: \"The weather is terrible.\" → Negative\n"
        f"Now classify: \"{sentence}\""
    )

if st.button("Classify Sentiment"):
    if sentence.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            output = response.text.strip()

            st.subheader("Result:")
            st.success(output)

        except Exception as e:
            st.error(f"Error: {e}")
