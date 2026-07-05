from pydantic import BaseModel


class DocumentInfo(BaseModel):
    id: str
    filename: str
    chunk_count: int


class Source(BaseModel):
    document_id: str
    filename: str
    chunk_id: str
    content: str
    score: float


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]

