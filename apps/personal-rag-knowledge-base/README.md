# 个人知识库问答系统

这是第三个完整实战项目。

目标：

```text
掌握 RAG 的完整链路：文档上传 -> 文本切分 -> 向量检索 -> 基于资料回答 -> 引用来源。
```

为了让初学者先跑通流程，本项目第一版使用本地 JSON 存储和简单文本向量检索。后续可以替换成：

```text
Embedding API + Qdrant
```

## 项目结构

```text
personal-rag-knowledge-base/
├─ frontend/           # Vue3 + Vite
├─ backend/            # FastAPI
├─ docker-compose.yml
├─ .env.example
└─ README.md
```

## 功能

- [x] 上传 txt / markdown
- [x] 文档解析
- [x] 文本切分
- [x] 本地向量化
- [x] 相似片段检索
- [x] RAG 问答
- [x] 引用来源
- [x] 文档列表
- [x] 删除文档
- [x] Docker Compose

## 本地启动

### 后端

```bash
cd apps/personal-rag-knowledge-base/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 前端

```bash
cd apps/personal-rag-knowledge-base/frontend
npm install
npm run dev
```

访问：

```text
http://localhost:5173
```

## Docker 启动

```bash
cd apps/personal-rag-knowledge-base
docker compose up --build
```

## 测试文档

可以上传：

```text
sample-documents/员工手册.md
```

然后提问：

```text
年假怎么算？
报销需要什么材料？
离职工资什么时候发？
```

## 学习目标

做完这个项目，你要能讲清楚：

- RAG 是什么
- 文档为什么要切分
- Embedding 和向量检索的作用
- 为什么要展示引用来源
- 为什么资料不足时要拒答
