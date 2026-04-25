from sentence_transformers import SentenceTransformer

# Load small embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(texts):
    return model.encode(texts)