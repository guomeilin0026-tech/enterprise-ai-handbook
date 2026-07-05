import json
import shutil
import uuid
from pathlib import Path

from app.text_splitter import split_text
from app.vectorizer import cosine_similarity, vectorize

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
INDEX_FILE = DATA_DIR / "index.json"


def ensure_data_dirs() -> None:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    if not INDEX_FILE.exists():
        INDEX_FILE.write_text(json.dumps({"documents": [], "chunks": []}, ensure_ascii=False, indent=2), encoding="utf-8")


def load_index() -> dict:
    ensure_data_dirs()
    return json.loads(INDEX_FILE.read_text(encoding="utf-8"))


def save_index(index: dict) -> None:
    ensure_data_dirs()
    INDEX_FILE.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def list_documents() -> list[dict]:
    index = load_index()
    documents = []
    for document in index["documents"]:
        chunk_count = sum(1 for chunk in index["chunks"] if chunk["document_id"] == document["id"])
        documents.append({**document, "chunk_count": chunk_count})
    return documents


def add_document(filename: str, content: str) -> dict:
    ensure_data_dirs()
    document_id = str(uuid.uuid4())
    safe_name = f"{document_id}_{Path(filename).name}"
    (UPLOAD_DIR / safe_name).write_text(content, encoding="utf-8")

    chunks = split_text(content)
    index = load_index()
    document = {"id": document_id, "filename": filename}
    index["documents"].append(document)

    for idx, chunk in enumerate(chunks):
        index["chunks"].append(
            {
                "id": f"{document_id}_{idx}",
                "document_id": document_id,
                "filename": filename,
                "content": chunk,
                "vector": vectorize(chunk),
            }
        )

    save_index(index)
    return {**document, "chunk_count": len(chunks)}


def delete_document(document_id: str) -> bool:
    index = load_index()
    before = len(index["documents"])
    index["documents"] = [item for item in index["documents"] if item["id"] != document_id]
    index["chunks"] = [item for item in index["chunks"] if item["document_id"] != document_id]
    save_index(index)

    for path in UPLOAD_DIR.glob(f"{document_id}_*"):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)

    return len(index["documents"]) < before


def search_chunks(question: str, top_k: int = 4) -> list[dict]:
    index = load_index()
    query_vector = vectorize(question)
    scored = []

    for chunk in index["chunks"]:
        score = cosine_similarity(query_vector, chunk["vector"])
        if score > 0:
            scored.append({**chunk, "score": round(score, 4)})

    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:top_k]

