import google.generativeai as genai
import streamlit as st

# Configure Gemini API
genai.configure(api_key= st.secrets["GEMINI_API_KEY"])
# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(question, context):

    prompt = f"""
    You are a helpful AI assistant.

    Answer the question ONLY using
    the provided context.

    If the answer is not present
    in the context, say:

    'Answer not found in document.'

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(prompt)
    
    return response.text