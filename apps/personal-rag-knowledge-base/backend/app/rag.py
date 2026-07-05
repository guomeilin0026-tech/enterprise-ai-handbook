from app.store import search_chunks


def answer_question(question: str) -> dict:
    sources = search_chunks(question)

    if not sources:
        return {
            "answer": "资料中没有找到相关信息。请先上传相关文档，或换一种问法。",
            "sources": [],
        }

    context = "\n".join(f"- {item['content']}" for item in sources)
    answer = (
        "根据已上传资料，我找到以下相关信息：\n\n"
        f"{context}\n\n"
        "教学版当前使用本地检索和 mock 回答。后续可以替换为真实大模型，让模型基于这些片段生成更自然的回答。"
    )

    return {
        "answer": answer,
        "sources": [
            {
                "document_id": item["document_id"],
                "filename": item["filename"],
                "chunk_id": item["id"],
                "content": item["content"],
                "score": item["score"],
            }
            for item in sources
        ],
    }

