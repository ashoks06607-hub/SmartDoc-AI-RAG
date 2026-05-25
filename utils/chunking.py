def chunk_text(text, chunk_size=500):   # Parameter	Meaning =  text : full PDF text, chunk_size : size of each chunk
    
    chunks = []  # This will hold our text pieces.
    
    for i in range(0, len(text), chunk_size): # Step through text in increments of chunk_size.
        chunk = text[i:i + chunk_size]  # Extract a piece of text.
        chunks.append(chunk)  # Add it to our list of chunks.
        
    return chunks  # Return the list of text chunks.
        