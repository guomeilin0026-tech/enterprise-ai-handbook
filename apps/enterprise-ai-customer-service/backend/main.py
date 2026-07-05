from pathlib import Path

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.deps import current_user
from app.schemas import AgentRequest, ChatRequest, KnowledgeBaseCreate, LoginRequest, LoginResponse
from app.store import (
    add_document,
    create_kb,
    find_user,
    list_documents,
    list_kbs,
    list_tool_logs,
    log_tool,
    log_usage,
    search_chunks,
    usage_summary,
)

app = FastAPI(title="Enterprise AI Customer Service")

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


@app.post("/api/auth/login", response_model=LoginResponse)
def login(request: LoginRequest):
    user = find_user(request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    return LoginResponse(token=f"demo-token-{user['id']}", username=user["username"], role=user["role"])


@app.get("/api/knowledge-bases")
def knowledge_bases(user: dict = Depends(current_user)):
    return list_kbs(user["id"])


@app.post("/api/knowledge-bases")
def create_knowledge_base(request: KnowledgeBaseCreate, user: dict = Depends(current_user)):
    return create_kb(user["id"], request.name, request.description)


@app.get("/api/documents")
def documents(knowledge_base_id: str, user: dict = Depends(current_user)):
    return list_documents(user["id"], knowledge_base_id)


@app.post("/api/documents/upload")
async def upload_document(
    knowledge_base_id: str,
    file: UploadFile = File(...),
    user: dict = Depends(current_user),
):
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in {".txt", ".md", ".markdown"}:
        raise HTTPException(status_code=400, detail="仅支持 txt、md、markdown")
    raw = await file.read()
    content = raw.decode("utf-8")
    try:
        return add_document(user["id"], knowledge_base_id, file.filename or "untitled.txt", content)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/api/chat")
def chat(request: ChatRequest, user: dict = Depends(current_user)):
    sources = search_chunks(user["id"], request.knowledge_base_id, request.question)
    if not sources:
        answer = "资料中没有找到相关信息。"
    else:
        context = "\n".join(f"- {item['content']}" for item in sources)
        answer = f"根据企业知识库资料，找到以下相关内容：\n\n{context}"
    log_usage(user["id"], "rag_chat", len(request.question), len(answer))
    return {"answer": answer, "sources": sources}


@app.post("/api/agent/run")
def run_agent(request: AgentRequest, user: dict = Depends(current_user)):
    if "订单" in request.task:
        tool_name = "get_order_status"
        arguments = {"order_id": "10086"}
        result = {"order_id": "10086", "status": "已发货", "estimate_time": "明天送达"}
        final_answer = "订单 10086 已发货，预计明天送达。"
    else:
        tool_name = "search_knowledge_base"
        arguments = {"query": request.task}
        result = {"message": "教学版 Agent 暂未连接真实业务系统"}
        final_answer = "我已完成工具调用模拟。真实项目中这里会连接企业业务系统。"

    log_tool(user["id"], tool_name, arguments, result)
    log_usage(user["id"], "agent", len(request.task), len(final_answer))
    return {"tool_name": tool_name, "arguments": arguments, "tool_result": result, "answer": final_answer}


@app.get("/api/usage/summary")
def usage(user: dict = Depends(current_user)):
    return usage_summary(user["id"])


@app.get("/api/agent/logs")
def agent_logs(user: dict = Depends(current_user)):
    return list_tool_logs(user["id"])

