# AI 简历优化助手

这是第二个完整实战项目。

目标：

```text
掌握 Prompt Engineering + Structured Output + 前端卡片展示。
```

默认使用 mock 分析结果，不需要 API Key 也能运行。配置 `.env` 后可以接 OpenAI-compatible API。

## 项目结构

```text
resume-ai-assistant/
├─ frontend/           # Vue3 + Vite
├─ backend/            # FastAPI
├─ docker-compose.yml
├─ .env.example
└─ README.md
```

## 功能

- [x] 输入简历
- [x] 输入岗位 JD
- [x] 后端 Prompt 模板
- [x] 结构化 JSON 输出
- [x] Pydantic 校验
- [x] Mock 分析结果
- [x] 前端卡片展示
- [x] Docker Compose

## 本地启动

### 后端

```bash
cd apps/resume-ai-assistant/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```

### 前端

```bash
cd apps/resume-ai-assistant/frontend
npm install
npm run dev
```

访问：

```text
http://localhost:5173
```

## Docker 启动

```bash
cd apps/resume-ai-assistant
copy .env.example .env
docker compose up --build
```

## 学习目标

做完这个项目，你要能讲清楚：

- Prompt 怎么设计
- 为什么结构化输出适合前端
- Pydantic 为什么要校验 AI 输出
- AI 输出 JSON 错了怎么办

