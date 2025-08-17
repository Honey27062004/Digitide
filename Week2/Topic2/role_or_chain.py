import streamlit as st
import google.generativeai as genai


API_KEY = "AIzaSyA1Cyn9KNTuwX-6rrMiXqCMuT6h-Q1WmqM" 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Role-based vs Chain-of-Thought Prompting")
st.write("Compare how Gemini responds when using Role-based or Chain-of-Thought prompts.")

topic = st.text_input("Enter a topic:", "")
mode = st.radio("Select Prompt Type:", ["Role-based", "Chain-of-Thought", "Both"])

if st.button("Generate Answer"):
    if topic.strip():
        if mode in ["Role-based", "Both"]:
            role_prompt = f"You are a high school biology teacher. Explain {topic} to students in simple words."
            role_response = model.generate_content(role_prompt)
        
        if mode in ["Chain-of-Thought", "Both"]:
            cot_prompt = f"Explain {topic} step by step, reasoning each step clearly."
            cot_response = model.generate_content(cot_prompt)

        if mode == "Role-based":
            st.subheader("Role-based Output")
            st.write(role_response.text)

        elif mode == "Chain-of-Thought":
            st.subheader("Chain-of-Thought Output")
            st.write(cot_response.text)

        elif mode == "Both":
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Role-based Output")
                st.write(role_response.text)
            with col2:
                st.subheader("Chain-of-Thought Output")
                st.write(cot_response.text)
    else:
        st.warning("Please enter a topic first.")
