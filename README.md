VeritasAI:

Trusted AI Document Assistant with Hallucination-Aware RAG Pipeline

VeritasAI is an intelligent document question-answering system built using Retrieval-Augmented Generation (RAG). The application allows users to upload PDF documents and receive context-grounded AI-generated answers with built-in hallucination detection.

The system combines semantic retrieval, vector search, and Gemini AI to generate reliable responses directly from uploaded documents instead of relying solely on pretrained LLM knowledge.

🚀 Live Demo:
Streamlit App: [https://smartdoc-ai-rag-jm6fnssyk72nguo8tidhws.streamlit.app/]
GitHub Repository: [https://github.com/ashoks06607-hub/SmartDoc-AI-RAG]

📌 Project Overview:

VeritasAI is designed to solve one of the biggest challenges in Generative AI systems:

LLM Hallucinations

Large Language Models can generate confident but factually incorrect answers when they lack proper context. VeritasAI reduces hallucinations by implementing a Retrieval-Augmented Generation (RAG) pipeline that retrieves relevant document chunks before generating responses.

The application enables users to:

Upload PDF documents
Ask questions related to document content
Retrieve context-aware answers
Verify answer grounding using semantic similarity scoring
Detect potential hallucinations

This project demonstrates practical implementation of modern GenAI engineering concepts including embeddings, vector databases, semantic retrieval, grounding verification, and cloud deployment.

✨ Features
📄 Upload and process PDF documents
🔍 Context-aware semantic retrieval
🤖 AI-generated document answers using Gemini AI
🧠 Retrieval-Augmented Generation (RAG) pipeline
📚 FAISS vector database integration
✅ Grounded answer verification
⚠️ Hallucination detection using similarity scoring
💬 Interactive Streamlit web interface
☁️ Cloud deployment using Streamlit Community Cloud
🔐 Secure API key management using Streamlit Secrets

🛠️ Tech Stack:

Frontend:
-Streamlit

Backend:
-Python

AI / Machine Learning:

-Gemini AI
-Sentence Transformers
-FAISS Vector Search
-Retrieval-Augmented Generation (RAG)

Libraries & Frameworks:

-PyPDF2
-NumPy
-Scikit-learn
-Transformers
-Torch

Deployment & Version Control
Git
GitHub
Streamlit Community Cloud


Development Flow:

PDF Upload
    ↓
PDF Text Extraction
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Storage
    ↓
Question Embedding
    ↓
Semantic Retrieval
    ↓
Gemini AI Response Generation
    ↓
Grounding Verification
    ↓
Hallucination Detection


