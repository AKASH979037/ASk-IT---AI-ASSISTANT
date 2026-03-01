from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.rag import generate_answer
from app.core.security import verify_token

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    question: str

@router.post("/")
def chat(req: ChatRequest, token: str = Depends(verify_token)):
    answer, confidence = generate_answer(req.question)
    return {
        "answer": answer,
        "confidence": confidence
    }