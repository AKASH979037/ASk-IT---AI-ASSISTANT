"""Pydantic models for request/response validation"""
from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    question: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    question: str
    answer: str
    sources: Optional[list] = None
    session_id: Optional[str] = None


class HealthResponse(BaseModel):
    """Response model for health endpoint"""
    status: str
    message: str
