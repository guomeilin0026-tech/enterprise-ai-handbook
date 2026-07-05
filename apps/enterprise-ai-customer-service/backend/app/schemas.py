from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    username: str
    role: str


class KnowledgeBaseCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = ""


class ChatRequest(BaseModel):
    knowledge_base_id: str
    question: str


class AgentRequest(BaseModel):
    task: str

