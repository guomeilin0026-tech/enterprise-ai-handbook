from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from app.llm import chat_once, chat_stream
from app.schemas import ChatRequest, ChatResponse

app = FastAPI(title="AI Chat Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="message 不能为空")

    reply = await chat_once(request.message, request.history)
    return ChatResponse(reply=reply)


@app.post("/api/chat/stream")
async def stream_chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="message 不能为空")

    async def event_stream():
        async for chunk in chat_stream(request.message, request.history):
            yield chunk

    return StreamingResponse(event_stream(), media_type="text/plain; charset=utf-8")

