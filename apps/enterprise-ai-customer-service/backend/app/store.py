import json
import uuid
from pathlib import Path

from app.text_splitter import split_text
from app.vectorizer import cosine_similarity, vectorize

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
INDEX_FILE = DATA_DIR / "db.json"


def default_data() -> dict:
    return {
        "users": [
            {"id": "u_admin", "username": "admin", "password": "admin123", "role": "admin"}
        ],
        "knowledge_bases": [],
        "documents": [],
        "chunks": [],
        "messages": [],
        "usage_logs": [],
        "tool_logs": [],
    }


def ensure_db() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not INDEX_FILE.exists():
        save_db(default_data())


def load_db() -> dict:
    ensure_db()
    return json.loads(INDEX_FILE.read_text(encoding="utf-8"))


def save_db(db: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def find_user(username: str, password: str) -> dict | None:
    db = load_db()
    for user in db["users"]:
        if user["username"] == username and user["password"] == password:
            return {key: value for key, value in user.items() if key != "password"}
    return None


def get_user_by_token(token: str) -> dict | None:
    if not token.startswith("demo-token-"):
        return None
    user_id = token.replace("demo-token-", "", 1)
    db = load_db()
    for user in db["users"]:
        if user["id"] == user_id:
            return {key: value for key, value in user.items() if key != "password"}
    return None


def create_kb(user_id: str, name: str, description: str) -> dict:
    db = load_db()
    item = {"id": str(uuid.uuid4()), "user_id": user_id, "name": name, "description": description}
    db["knowledge_bases"].append(item)
    save_db(db)
    return item


def list_kbs(user_id: str) -> list[dict]:
    return [item for item in load_db()["knowledge_bases"] if item["user_id"] == user_id]


def add_document(user_id: str, kb_id: str, filename: str, content: str) -> dict:
    db = load_db()
    if not any(kb["id"] == kb_id and kb["user_id"] == user_id for kb in db["knowledge_bases"]):
        raise ValueError("知识库不存在")

    document = {"id": str(uuid.uuid4()), "user_id": user_id, "knowledge_base_id": kb_id, "filename": filename}
    db["documents"].append(document)

    chunks = split_text(content)
    for idx, chunk in enumerate(chunks):
        db["chunks"].append(
            {
                "id": f"{document['id']}_{idx}",
                "user_id": user_id,
                "knowledge_base_id": kb_id,
                "document_id": document["id"],
                "filename": filename,
                "content": chunk,
                "vector": vectorize(chunk),
            }
        )

    save_db(db)
    return {**document, "chunk_count": len(chunks)}


def list_documents(user_id: str, kb_id: str) -> list[dict]:
    db = load_db()
    docs = [item for item in db["documents"] if item["user_id"] == user_id and item["knowledge_base_id"] == kb_id]
    result = []
    for doc in docs:
        count = sum(1 for chunk in db["chunks"] if chunk["document_id"] == doc["id"])
        result.append({**doc, "chunk_count": count})
    return result


def search_chunks(user_id: str, kb_id: str, question: str, top_k: int = 4) -> list[dict]:
    db = load_db()
    query_vector = vectorize(question)
    scored = []
    for chunk in db["chunks"]:
        if chunk["user_id"] != user_id or chunk["knowledge_base_id"] != kb_id:
            continue
        score = cosine_similarity(query_vector, chunk["vector"])
        if score > 0:
            scored.append({**chunk, "score": round(score, 4)})
    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:top_k]


def log_usage(user_id: str, action: str, input_size: int, output_size: int) -> None:
    db = load_db()
    db["usage_logs"].append(
        {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "action": action,
            "input_tokens": max(1, input_size // 2),
            "output_tokens": max(1, output_size // 2),
        }
    )
    save_db(db)


def usage_summary(user_id: str) -> dict:
    logs = [item for item in load_db()["usage_logs"] if item["user_id"] == user_id]
    return {
        "requests": len(logs),
        "input_tokens": sum(item["input_tokens"] for item in logs),
        "output_tokens": sum(item["output_tokens"] for item in logs),
    }


def log_tool(user_id: str, tool_name: str, arguments: dict, result: dict) -> dict:
    db = load_db()
    item = {
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "tool_name": tool_name,
        "arguments": arguments,
        "result": result,
    }
    db["tool_logs"].append(item)
    save_db(db)
    return item


def list_tool_logs(user_id: str) -> list[dict]:
    return [item for item in load_db()["tool_logs"] if item["user_id"] == user_id]

