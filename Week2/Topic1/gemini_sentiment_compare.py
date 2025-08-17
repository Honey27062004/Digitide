import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyA1Cyn9KNTuwX-6rrMiXqCMuT6h-Q1WmqM")

st.title("Zero-shot vs Few-shot Prompting - Sentiment Analysis")

sentence = st.text_input("Enter a sentence to classify sentiment:")

def get_sentiment(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

if st.button("Classify Sentiment"):
    if sentence.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        
        zero_shot_prompt = f"Determine if the following sentence is positive or negative: \"{sentence}\""

        few_shot_prompt = (
            "Example 1: \"I am happy today.\" → Positive\n"
            "Example 2: \"I am sad today.\" → Negative\n"
            "Example 3: \"The weather is terrible.\" → Negative\n"
            f"Now classify: \"{sentence}\""
        )

        try:
         
            zero_shot_output = get_sentiment(zero_shot_prompt)
            few_shot_output = get_sentiment(few_shot_prompt)

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Zero-shot Output")
                st.success(zero_shot_output)

            with col2:
                st.subheader("Few-shot Output")
                st.success(few_shot_output)

        except Exception as e:
            st.error(f"Error: {e}")
