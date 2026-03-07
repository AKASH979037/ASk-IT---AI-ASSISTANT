"""Test suite for FastAPI endpoints"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_chat_with_valid_question():
    """Test chat endpoint with valid question"""
    response = client.post(
        "/chat",
        json={"question": "What is AI?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "question" in data
    assert data["question"] == "What is AI?"


def test_chat_with_session_id():
    """Test chat endpoint with session ID"""
    response = client.post(
        "/chat",
        json={
            "question": "Explain machine learning",
            "session_id": "test_session_123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["session_id"] == "test_session_123"


def test_chat_with_empty_question():
    """Test chat endpoint with empty question"""
    response = client.post(
        "/chat",
        json={"question": ""}
    )
    assert response.status_code == 400


def test_chat_with_whitespace_question():
    """Test chat endpoint with whitespace-only question"""
    response = client.post(
        "/chat",
        json={"question": "   "}
    )
    assert response.status_code == 400


def test_chat_response_structure():
    """Test that chat response has correct structure"""
    response = client.post(
        "/chat",
        json={"question": "Test question"}
    )
    assert response.status_code == 200
    data = response.json()
    
    assert "question" in data
    assert "answer" in data
    assert "sources" in data
    
    assert isinstance(data["question"], str)
    assert isinstance(data["answer"], str)
    assert isinstance(data["sources"], (list, type(None)))
