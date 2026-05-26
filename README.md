# VeritasAI

### Trusted AI Document Assistant with Hallucination-Aware RAG Pipeline

VeritasAI is a document question-answering application built using Retrieval-Augmented Generation (RAG). The system allows users to upload PDF documents and receive context-aware AI-generated answers grounded directly in the uploaded content.

The project was developed to address one of the key challenges in Generative AI systems: hallucinations. Instead of relying only on pretrained LLM knowledge, VeritasAI retrieves relevant document context before generating responses, improving answer reliability and transparency.

---

# Live Demo

- Streamlit Application: [https://smartdoc-ai-rag-jm6fnssyk72nguo8tidhws.streamlit.app/]
- GitHub Repository: [https://github.com/ashoks06607-hub/SmartDoc-AI-RAG]

---

# Project Overview

Large Language Models can sometimes generate confident but incorrect responses when proper context is unavailable. VeritasAI reduces this issue by implementing a Retrieval-Augmented Generation pipeline that retrieves relevant sections from uploaded documents before generating answers.

The application enables users to:

- Upload PDF documents
- Ask questions related to the document
- Retrieve context-aware answers
- Verify whether generated responses are grounded in retrieved context
- Detect potentially unreliable or hallucinated responses

This project demonstrates practical implementation of modern Generative AI concepts including embeddings, vector search, semantic retrieval, grounding verification, and cloud deployment.

---

# Features

- PDF document upload and processing
- Context-aware semantic retrieval
- AI-generated answers using Gemini AI
- Retrieval-Augmented Generation (RAG) pipeline
- FAISS vector database integration
- Grounding verification using semantic similarity
- Hallucination detection workflow
- Interactive Streamlit interface
- Cloud deployment using Streamlit Community Cloud
- Secure API key management using Streamlit Secrets

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI / Machine Learning
- Gemini AI
- Sentence Transformers
- FAISS Vector Search
- Retrieval-Augmented Generation (RAG)

## Libraries
- PyPDF2
- NumPy
- Scikit-learn
- Transformers
- Torch

## Deployment & Version Control
- Git
- GitHub
- Streamlit Community Cloud

---

# Project Workflow

## Development Workflow

```text
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
```

---

## Local Development Process

The project was initially developed and tested locally using Python virtual environments and VS Code. The backend was designed in a modular structure to separate PDF loading, chunking, embedding generation, retrieval, and grounding verification into individual utility modules.

---

## GitHub Version Control Workflow

The project uses Git and GitHub for version tracking and deployment integration.

### Initialize Repository

```bash
git init
```

### Add Files

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Initial commit"
```

### Push to GitHub

```bash
git push origin main
```

---

## Streamlit Deployment Workflow

```text
GitHub Repository
        ↓
Streamlit Cloud Integration
        ↓
Dependency Installation
        ↓
Secrets Configuration
        ↓
Application Deployment
        ↓
Live Application
```

---

## Updating and Redeploying

Whenever updates are made to the application:

```bash
git add .
git commit -m "Updated application"
git push
```

Streamlit automatically redeploys the latest version of the project after new commits are pushed to GitHub.

---

# Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/ashoks06607-hub/LLM-Hallucination-Detection-System.git
```

---

## 2. Navigate to Project Directory

```bash
cd veritas-ai
```

---

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Configure Gemini API Key

Create the following file locally:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY="your_api_key_here"
```

---

## 7. Run the Application

```bash
streamlit run app.py
```

---

# Deployment Process

The application was deployed using Streamlit Community Cloud with GitHub integration.

## Deployment Steps

### 1. Push Project to GitHub

```bash
git add .
git commit -m "Deployment ready"
git push
```

---

### 2. Open Streamlit Community Cloud

Visit:

```text
https://share.streamlit.io
```

---

### 3. Connect GitHub Repository

- Login using GitHub
- Select the repository
- Select the `main` branch
- Choose `app.py` as the entry point

---

### 4. Configure Streamlit Secrets

Inside Streamlit Cloud, add:

```toml
GEMINI_API_KEY="your_actual_api_key"
```

---

### 5. Deploy the Application

Click the deploy button. Streamlit automatically installs dependencies, builds the project, and deploys the live application.

---

# Folder Structure

```text
veritas-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── documents/
│   └── sample.pdf
│
├── utils/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── grounding.py
│   └── llm_gemini.py
│
├── vector_store/
│
└── venv/
```

---

# Usage Instructions

## 1. Upload a PDF

Users can upload any supported PDF document through the Streamlit interface.

---

## 2. Ask Questions

Example:

```text
What are the major risks discussed in the document?
```

---

## 3. AI Response Generation

The application retrieves semantically relevant chunks from the uploaded document and generates grounded responses using Gemini AI.

---

## 4. Grounding Verification

The generated response is compared with retrieved document context to calculate a grounding score and detect possible hallucinations.

---

# Future Improvements

Potential future enhancements include:

- Multi-document support
- Conversational memory
- Chat history persistence
- Source citation highlighting
- OCR support for scanned PDFs
- Advanced hallucination scoring
- Docker containerization
- Authentication system
- Persistent vector database storage
- Multi-LLM support (OpenAI, Claude, Ollama)

---

# Contributing

Contributions are welcome.

## Contribution Workflow

### Create Feature Branch

```bash
git checkout -b feature-name
```

### Commit Changes

```bash
git commit -m "Added new feature"
```

### Push Changes

```bash
git push origin feature-name
```

### Open Pull Request

Please ensure:
- Code is clean and documented
- Commits are meaningful
- Features are tested before submission

---

# License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software...
```

---

# Contact

**[ASHOK S]**

- GitHub: [https://github.com/ashoks06607-hub]
- LinkedIn: [www.linkedin.com/in/ashok-s-7572b5364]
- Email: [ashoks06607@gmail.com]

---

# Acknowledgements

This project was built using tools and libraries from the open-source AI ecosystem, including:

- Google Gemini AI
- Streamlit
- Hugging Face
- FAISS
- Sentence Transformers
