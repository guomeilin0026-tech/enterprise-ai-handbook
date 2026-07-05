from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minimal AI Chat Example")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Replace this mock reply with a real LLM API call later.
    return ChatResponse(reply=f"AI received your question: {request.message}")

