#supabse_client.py

from supabase import create_client, Client
import streamlit as st

@st.cache_resource

def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url,key)

def upload_embedding(filename: str, filetype: str, embedding):
    data = {"filename": filename, "filetype": filetype, "embedding": embedding}
    supabase.table("embeddings").insert(data).execute()

