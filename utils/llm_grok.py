import streamlit as st
from openai import OpenAI

# Create Client
client = OpenAI( api_key=st.secrets["GROK_API_KEY"],  base_url="https://api.x.ai/v1")


def generate_answer(question, context):

    prompt = f"""
    You are a helpful AI assistant.

    Answer the question ONLY using
    the provided context.

    If answer is not found in context,
    say:
    'Answer not found in document.'

    Context:
    {context}

    Question:
    {question}
    """


    response = client.chat.completions.create(

        model="grok-2-latest",messages=[{"role": "user","content": prompt}],temperature=0)

    return response.choices[0].message.content