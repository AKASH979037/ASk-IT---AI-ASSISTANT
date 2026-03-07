"""FastAPI Application for ASK-IT AI Assistant"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging
import os
from typing import Optional

from models import ChatRequest, ChatResponse, HealthResponse
from rag_service import RAGPipeline

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="ASK-IT AI Assistant",
    description="RAG-based AI Assistant API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG Pipeline
rag_pipeline = RAGPipeline()


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    logger.info("ASK-IT API Starting up...")
    logger.info("RAG Pipeline initialized")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("ASK-IT API Shutting down...")


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint
    
    Returns:
        Health status of the API
    """
    return HealthResponse(
        status="healthy",
        message="ASK-IT API is running"
    )


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint - Process user question through RAG pipeline
    
    Flow:
    1. Receive question from UI
    2. Call RAG pipeline to retrieve documents and generate response
    3. Return answer with sources to UI
    
    Args:
        request: ChatRequest with question and optional session_id
        
    Returns:
        ChatResponse with answer and sources
        
    Raises:
        HTTPException: If processing fails
    """
    try:
        logger.info(f"Received chat request: {request.question}")
        
        # Validate input
        if not request.question or not request.question.strip():
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )
        
        # Step 1: Call RAG pipeline
        result = rag_pipeline.process_query(request.question)
        
        # Step 2: Prepare response
        response = ChatResponse(
            question=request.question,
            answer=result.get("answer"),
            sources=result.get("sources"),
            session_id=request.session_id
        )
        
        logger.info(f"Chat request processed successfully")
        return response
        
    except HTTPException as e:
        logger.error(f"HTTP Error: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request"
        )


@app.post("/hello")
async def hello(request: ChatRequest):
    """
    Simple hello endpoint - Returns hello when JSON is passed
    
    Args:
        request: ChatRequest with question
        
    Returns:
        Hello message response
    """
    return {
        "message": "The chat bot is under development and we appreciate your patience. Please check back soon for updates!",
        "received_question": request.question
    }


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to ASK-IT AI Assistant API",
        "docs": "/docs",
        "health": "/health"
    }


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=os.getenv("ENV", "development") == "development"
    )
