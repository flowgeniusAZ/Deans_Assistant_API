#embeddings.py

import openai
import streamlit as st

# Configure your OpenAI API key here
openai.api_key = st.secrets["OPEN_API_KEY"]

def generate_embedding(text, model="text-similarity-davinci-001"):
    response = openai.Embedding.create(
        input=[text],
        model=model
    )
    embedding = response['data'][0]['embedding']
    return embedding
