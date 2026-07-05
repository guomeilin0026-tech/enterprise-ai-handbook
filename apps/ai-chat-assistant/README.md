# AI 聊天助手

这是第一个完整实战项目。

目标：

```text
跑通 Vue3 前端 + FastAPI 后端 + 大模型 API 的最小闭环。
```

默认使用 mock AI 回复，不需要 API Key 也能跑。配置 `.env` 后可以接 OpenAI-compatible API。

## 项目结构

```text
ai-chat-assistant/
├─ frontend/           # Vue3 + Vite
├─ backend/            # FastAPI
├─ docker-compose.yml
├─ .env.example
└─ README.md
```

## 功能

- [x] Vue3 聊天页面
- [x] FastAPI `/api/chat` 接口
- [x] FastAPI `/api/chat/stream` 流式接口
- [x] 后端读取 `.env`
- [x] Mock AI 回复
- [x] 预留真实大模型 API
- [x] 前端展示 AI 回复
- [x] loading 状态
- [x] 错误提示
- [x] 停止生成
- [x] 流式输出

## 本地启动

### 1. 启动后端

```bash
cd apps/ai-chat-assistant/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```

后端地址：

```text
http://127.0.0.1:8000
```

接口文档：

```text
http://127.0.0.1:8000/docs
```

### 2. 启动前端

```bash
cd apps/ai-chat-assistant/frontend
npm install
npm run dev
```

前端地址：

```text
http://localhost:5173
```

## Docker 启动

```bash
cd apps/ai-chat-assistant
copy .env.example .env
docker compose up --build
```

访问：

```text
http://localhost:5173
```

## 接真实大模型 API

编辑 `.env`：

```text
USE_MOCK_LLM=false
OPENAI_API_KEY=你的 key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4.1-mini
```

如果使用其他 OpenAI-compatible 服务，修改 `OPENAI_BASE_URL` 和 `OPENAI_MODEL` 即可。

## 学习目标

做完这个项目，你要能讲清楚：

- 为什么 API Key 不能放前端
- 前端如何请求后端
- 后端如何调用模型
- 什么是流式输出
- 为什么要有错误处理和停止生成

## 验收清单

- [ ] 后端 `/health` 正常
- [ ] 前端能打开
- [ ] 输入问题后能看到 mock 回复
- [ ] 流式输出能逐步显示
- [ ] 停止按钮能中断生成
- [ ] 配置真实 API 后能收到模型回复
