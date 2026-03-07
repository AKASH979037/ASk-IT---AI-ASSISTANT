# FastAPI RAG Pipeline Implementation

## Overview
This FastAPI application implements a Retrieval-Augmented Generation (RAG) pipeline for the ASK-IT AI Assistant. The architecture follows this flow:

```
UI sends question
    ↓
POST /chat
    ↓
FastAPI route receives request
    ↓
Calls RAG pipeline
    ↓
Pipeline calls Retriever + LLM
    ↓
Answer returned
    ↓
FastAPI sends JSON response
    ↓
UI displays answer
```

## Project Structure

```
fastapi/
├── main.py              # FastAPI application with endpoints
├── models.py            # Pydantic models for request/response validation
├── rag_service.py       # RAG pipeline, Retriever, and LLM services
└── .env.example         # Environment configuration template
```

## Components

### 1. **main.py** - FastAPI Application
- **GET /health** - Health check endpoint
- **POST /chat** - Main chat endpoint that processes questions through RAG pipeline
- **GET /** - Root endpoint with API information

### 2. **models.py** - Data Models
- `ChatRequest` - Request model with question and optional session_id
- `ChatResponse` - Response model with answer, sources, and session_id
- `HealthResponse` - Health check response model

### 3. **rag_service.py** - RAG Pipeline Components

#### Retriever Class
- Handles document retrieval from vector stores
- Method: `retrieve(query, top_k=5)` - Returns relevant documents

#### LLMService Class
- Generates responses using retrieved context
- Method: `generate_response(question, context)` - Returns AI-generated answer

#### RAGPipeline Class
- Orchestrates the complete RAG workflow
- Method: `process_query(question)` - Executes: Retrieve → Build Context → Generate Response

## Setup Instructions

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the `fastapi` folder:

```bash
cp fastapi/.env.example fastapi/.env
```

Edit `.env` with your configuration:
```
PORT=8000
ENV=development
CORS_ORIGINS=http://localhost:3000,http://localhost:8000

# Configure your LLM provider
OPENAI_API_KEY=your_api_key_here

# Configure your vector store
PINECONE_API_KEY=your_api_key_here
PINECONE_INDEX=your_index_name
```

### 3. Run the FastAPI Server

```bash
cd fastapi
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## API Endpoints

### Health Check
```bash
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "ASK-IT API is running"
}
```

### Chat Endpoint
```bash
POST /chat
Content-Type: application/json

{
  "question": "What is machine learning?",
  "session_id": "optional_session_id"
}
```

**Response:**
```json
{
  "question": "What is machine learning?",
  "answer": "Machine learning is a subset of artificial intelligence...",
  "sources": ["document_1.pdf", "document_2.pdf"],
  "session_id": "optional_session_id"
}
```

## Implementation Notes

### TODO Items (Integrate Your Services)

1. **Vector Store Integration** (in `rag_service.py` - `Retriever` class):
   - Replace placeholder with your vector store (Pinecone, Weaviate, Chroma, etc.)
   - Implement embedding generation
   - Implement similarity search

2. **LLM Integration** (in `rag_service.py` - `LLMService` class):
   - Replace placeholder with your LLM (OpenAI, HuggingFace, Local model, etc.)
   - Implement prompt engineering
   - Handle model responses

### Example Integrations

#### Using OpenAI:
```python
import openai

class LLMService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def generate_response(self, question: str, context: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self._build_prompt(question, context)}]
        )
        return response.choices[0].message.content
```

#### Using Pinecone:
```python
import pinecone
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self):
        pinecone.init(api_key=os.getenv("PINECONE_API_KEY"))
        self.index = pinecone.Index(os.getenv("PINECONE_INDEX"))
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
    
    def retrieve(self, query: str, top_k: int = 5):
        embedding = self.encoder.encode(query)
        results = self.index.query(embedding, top_k=top_k, include_metadata=True)
        return results['matches']
```

## Frontend Integration

Update your React frontend to call the FastAPI endpoint:

```javascript
// In your React component
const sendMessage = async (question) => {
  const response = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question, session_id: 'user_session' })
  });
  const data = await response.json();
  return data;
};
```

## Error Handling

The API includes comprehensive error handling:
- **400**: Invalid request (empty question)
- **500**: Server error during processing
- **CORS**: Configured for frontend communication

## Logging

All operations are logged:
- Startup/shutdown events
- Chat request processing
- Retriever and LLM operations
- Errors with stack traces

Access logs via console or configure file-based logging.

## Production Deployment

For production, consider:
1. Use `gunicorn` with `uvicorn` workers
2. Add authentication (JWT, API keys)
3. Implement rate limiting
4. Add request validation and sanitization
5. Use environment-specific configurations
6. Deploy with Docker

**Example gunicorn command:**
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 main:app
```

## Next Steps

1. Choose and integrate a vector store (Pinecone, Weaviate, Chroma, etc.)
2. Choose and integrate an LLM provider (OpenAI, HuggingFace, Replicate, etc.)
3. Implement document indexing pipeline
4. Add authentication and rate limiting
5. Deploy to production (AWS, GCP, Azure, etc.)
