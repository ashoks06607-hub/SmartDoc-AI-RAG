import streamlit as st
from utils.pdf_loader import load_pdf
from utils.chunking import chunk_text
from utils.embeddings import (create_embeddings,model)
from utils.retrieval import (create_vector_store,retrieve_chunks)
from utils.llm_gemini import generate_answer
from utils.grounding import (check_grounding)


# Page Config
st.set_page_config(
    page_title="Veritas AI",
    page_icon="🤖",
    layout="wide")

# Sidebar

with st.sidebar:

    st.title("🤖 Veritas AI")

    st.markdown("""
    ### AI-Powered Document Assistant

    Upload PDFs and get intelligent, context-aware answers with built-in hallucination detection.
    """)

    st.divider()

    st.markdown("### Tech Stack")

    st.markdown("""
    - Streamlit
    - FAISS
    - Sentence Transformers
    - Gemini AI
    """)

    st.divider()

    st.markdown("### Features")

    st.markdown("""
    -  PDF Question Answering
    -  AI-Generated Responses
    -  Grounded Answer Verification
    -  Context-Aware Retrieval
    -  Hallucination Detection
    """)

# Header

st.title("🤖 VeritasAI")

st.markdown("""
### Hallucination-Aware RAG Assistant

Upload a PDF and receive context-grounded AI answers with hallucination detection.
""")

# Upload PDF
uploaded_file = st.file_uploader("Upload Your PDF",type="pdf")

if uploaded_file is not None:

    with open("temp.pdf","wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing PDF..."):

        text = load_pdf("temp.pdf")

        chunks = chunk_text(text)

        embeddings = create_embeddings(chunks)

        vector_store = create_vector_store(embeddings)

    st.success("PDF Processed Successfully")

    question = st.text_input("Ask a Question")

    if question:
        with st.spinner("Generating Answer..."):

            question_embedding = model.encode([question])

            retrieved_chunks = retrieve_chunks(
                question_embedding,
                vector_store,
                chunks)

            context = "\n".join( retrieved_chunks )  # Combine retrieved chunks into one context string for the LLM.

            answer = generate_answer( question,context)

            score = check_grounding(answer,context)

        st.subheader("AI Answer")

        st.write(answer)


        st.subheader("Grounding Score")

        st.write(round(score, 2))


        if score > 0.75:

            st.success( "✅ Grounded Answer")

        else:

            st.warning("⚠️ Possible Hallucination (Low Grounding Score)")


        with st.expander("Retrieved Context" ):
            
            st.write(context)