# 企业知识库 + 智能客服系统

这是最终综合项目。

目标：

```text
把登录、知识库、文档管理、RAG 问答、Agent 工具、用量统计和部署整合成一个企业 AI 应用。
```

第一版采用本地 JSON 存储和教学版 RAG，方便从 0 跑通企业 AI 应用闭环。

## 功能

- [x] 用户登录
- [x] 知识库管理
- [x] 文档上传
- [x] 文档切分
- [x] RAG 问答
- [x] 引用来源
- [x] Agent 工具模拟
- [x] 用量统计
- [x] Docker Compose

## 默认账号

```text
用户名：admin
密码：admin123
```

## 本地启动

### 后端

```bash
cd apps/enterprise-ai-customer-service/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 前端

```bash
cd apps/enterprise-ai-customer-service/frontend
npm install
npm run dev
```

访问：

```text
http://localhost:5173
```

## Docker 启动

```bash
cd apps/enterprise-ai-customer-service
copy .env.example .env
docker compose up --build
```

## 测试流程

1. 使用 `admin / admin123` 登录。
2. 新建一个知识库。
3. 上传 `sample-documents/客服知识库.md`。
4. 在智能客服里提问：`年假怎么算？`
5. 在 Agent 里输入：`帮我查订单 10086 的状态`
