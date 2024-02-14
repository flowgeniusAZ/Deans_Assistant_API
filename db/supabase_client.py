#supabse_client.py

from supabase import create_client, Client

supabase: Client = create_client(url, key)

def upload_embedding(filename: str, filetype: str, embedding):
    data = {"filename": filename, "filetype": filetype, "embedding": embedding}
    supabase.table("embeddings").insert(data).execute()
