# 个人知识库问答系统后端

## 启动

```bash
cd apps/personal-rag-knowledge-base/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

接口文档：

```text
http://127.0.0.1:8000/docs
```

## 接口

```text
GET /health
GET /api/documents
POST /api/documents/upload
DELETE /api/documents/{document_id}
POST /api/chat
```

## 教学说明

第一版使用本地 JSON 和简单向量检索，方便理解 RAG 流程。

真实企业项目可以升级为：

```text
Embedding API + Qdrant + PostgreSQL
```

