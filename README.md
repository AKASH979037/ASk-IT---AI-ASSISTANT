# AskIt — AI Chatbot Assistant

AskIt is a RAG-based (Retrieval Augmented Generation) AI chatbot system designed for small-scale businesses and institutions.  
It provides intelligent responses strictly from client-uploaded private data while ensuring complete data confidentiality.

This project is built as a Final Semester Project.

---

## 🚀 Project Overview

AskIt allows organizations to:

- Upload their internal documents (PDF / CSV)
- Automatically convert them into embeddings
- Enable an AI chatbot that answers only from their data
- Maintain full data privacy using a locally hosted LLM
- View unanswered questions and user feedback
- Export logs for improvement analysis

---

## 🏗 System Architecture

Client Website → Chat Widget → FastAPI Backend → RAG Pipeline → Local LLM (Ollama) → Response

The system uses:
- Multi-tenancy
- Role-based authentication
- Confidence-based fallback system
- Feedback logging

---

## 🛠 Tech Stack

### 🔹 Backend
- **FastAPI** — REST API framework
- **Python 3.10+**
- **SQLite** — Lightweight database
- **JWT + bcrypt** — Admin authentication
- **Firebase Authentication** — Google OAuth for users
- **SlowAPI** — Rate limiting

### 🔹 AI / RAG Stack
- **LangChain** — RAG orchestration
- **ChromaDB** — Vector database
- **sentence-transformers** — Embedding model
- **Ollama** — Local LLM engine
- **Mistral 7B** — Open-source large language model

### 🔹 Data Processing
- **PyMuPDF** — PDF text extraction
- **Pandas** — CSV processing
- **OpenPyXL** — Excel export

### 🔹 Frontend
- **React.js** — Admin dashboard
- **HTML / CSS / JavaScript** — Chat widget UI

### 🔹 Deployment
- **Render.com / Streamlit Cloud**
- **GitHub** — Version control

---

## 🔐 Security Features

- Local LLM (no external API calls)
- Client-based data isolation
- JWT token authentication
- Password hashing using bcrypt
- Rate limiting to prevent abuse

---

## 📂 Project Structure
