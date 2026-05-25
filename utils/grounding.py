from sklearn.metrics.pairwise import cosine_similarity  # Import cosine similarity function 
# to compare semantic meaning of the AI's answer and the retrieved context.

from utils.embeddings import model  # Import our embedding model

def check_grounding(answer, context):
    answer_embedding = model.encode([answer])  # Convert the AI's answer into an embedding vector.
    context_embedding = model.encode([context])  # Convert the retrieved context into an embedding vector
    
    similarity_score = cosine_similarity(answer_embedding, context_embedding)[0][0]  # Calculate cosine similarity between answer and context embeddings.
    return similarity_score  # Return the similarity score, which indicates how well the answer is grounded in the context.

