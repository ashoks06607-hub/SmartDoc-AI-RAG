import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# Load Gemini model
model = genai.GenerativeModel( "gemini-3.5-flash")


def generate_answer(question, context):

    prompt = f"""
    You are a helpful AI assistant.

    Answer ONLY using the provided context.

    If answer is not present in context,
    say:
    'Answer not found in document.'

    Context:
    {context}

    Question:
    {question}
    """


    response = model.generate_content(prompt)

    return response.text