import faiss
import numpy as np

def create_vector_store(embeddings):
    
    dimension = embeddings.shape[1] # Get the dimensionality of the embeddings. FAISS MUST know vector size because every vector must have same dimensions.
    
    index = faiss.IndexFlatL2(dimension)   # Create a FAISS index for L2 distance. L2 = Euclidean distance, closer vectors = semantically similar
    index.add(np.array(embeddings))     # Add our embeddings to the index in numpy array format. which works very fast in semantic similarity search.
    return index

def retrieve_chunks(         # This function will find the most relevant text chunks based on the question embedding.
    question_embedding,      # vector version of question
    vector_store,            # FAISS database
    chunks,                  # original text chunks (to retrieve actual text, not just vectors)
    k=3):                    # retrieve top 3 chunks

    distances, indices = vector_store.search(np.array(question_embedding), k)  # Search FAISS index for closest vectors to question embedding. Returns distances and indices of top k matches.

    retrieved_chunks = [] # create empty list to hold the actual text of the retrieved chunks.

    for idx in indices[0]:

        retrieved_chunks.append(chunks[idx])  # Converts chunk numbers back into readable text.

    return retrieved_chunks