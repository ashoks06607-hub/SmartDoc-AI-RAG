from sentence_transformers import SentenceTransformer  # Imports embedding model class


model = SentenceTransformer('all-MiniLM-L6-v2')    #This is NOT an LLM. This model ONLY creates embeddings.


def create_embeddings(chunks):

    embeddings = model.encode(chunks)  # This converts our text chunks into vectors (embeddings).

    return embeddings