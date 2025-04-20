import os
from supabase import create_client
from langchain_google_genai import GoogleGenerativeAIEmbeddings

os.environ["GOOGLE_API_KEY"] = "AIzaSyBETOFSRj3wJjAA8L5BPjHV47j_Es7Xu0w"
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


supabase_url = "https://pfzqdbextqywfvnxxuiy.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBmenFkYmV4dHF5d2Z2bnh4dWl5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTA3OTA5NiwiZXhwIjoyMDYwNjU1MDk2fQ.SRouGf68syeelbQyKr6jyVfti-XoSau6gSLbuVEGt58"
supabase = create_client(supabase_url, supabase_key)

def store_chat_in_supabase(user_msg: str, assistant_msg: str):
    try:
        combined_text = f"User: {user_msg}\nAssistant: {assistant_msg}"
        vector = embedding_model.embed_query(combined_text)

        response = supabase.table("chat_embeddings").insert([{
            "user_message": user_msg,
            "assistant_message": assistant_msg,
            "embedding": vector  
        }]).execute()

    except Exception as e:
        print("Error occured!")
