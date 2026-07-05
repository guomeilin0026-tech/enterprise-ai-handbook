# AI 简历优化助手后端

## 启动

```bash
cd apps/resume-ai-assistant/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```

接口文档：

```text
http://127.0.0.1:8000/docs
```

## 接口

```text
GET /health
POST /api/resume/analyze
```

默认 `USE_MOCK_LLM=true`，不需要真实 API Key。

