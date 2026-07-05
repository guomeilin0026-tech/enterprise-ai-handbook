# AI 聊天助手后端

技术栈：

```text
Python + FastAPI
```

## 启动

```bash
cd apps/ai-chat-assistant/backend
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
POST /api/chat
POST /api/chat/stream
```

## Mock 模式

默认 `USE_MOCK_LLM=true`，不需要真实 API Key 也能运行。

要接真实 OpenAI-compatible API：

```text
USE_MOCK_LLM=false
OPENAI_API_KEY=你的 key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4.1-mini
```
