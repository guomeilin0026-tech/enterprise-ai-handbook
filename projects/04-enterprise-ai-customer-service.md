# 项目 4：企业知识库 + 智能客服系统

## 项目定位

这是最终毕业项目，也是最适合写进简历的企业级 AI 应用。

## 业务背景

企业内部有大量制度、产品文档、客服手册和培训资料。员工或客户经常重复提问，人工回答成本高，信息查找效率低。

本项目通过 RAG 和大模型构建智能客服系统，让用户可以基于企业文档提问，并获得带引用来源的回答。

## 目标用户

- 企业员工
- 客服人员
- 管理员
- 业务部门成员

## 核心功能

### 用户系统

- [ ] 注册
- [ ] 登录
- [ ] JWT 鉴权
- [ ] 用户角色

### 知识库管理

- [ ] 新建知识库
- [ ] 编辑知识库
- [ ] 删除知识库
- [ ] 知识库列表

### 文档管理

- [ ] 上传文档
- [ ] 解析文档
- [ ] 文档切分
- [ ] 向量化入库
- [ ] 文档状态
- [ ] 删除文档

### AI 问答

- [ ] 选择知识库
- [ ] 输入问题
- [ ] RAG 检索
- [ ] 流式回答
- [ ] 引用来源
- [ ] 聊天记录

### Agent 工具

- [ ] 查询知识库
- [ ] 查询用户信息
- [ ] 查询工单状态
- [ ] 展示工具调用过程

### 管理后台

- [ ] 用户管理
- [ ] 模型配置
- [ ] Token 用量统计
- [ ] 用户反馈
- [ ] 日志查看

## 技术架构

```text
Vue3 + TypeScript
FastAPI
PostgreSQL
Qdrant
大模型 API
Docker Compose
Nginx
```

## 数据表

- users
- knowledge_bases
- documents
- document_chunks
- conversations
- messages
- model_usage_logs
- feedbacks
- tool_call_logs

## API 模块

- `/api/auth`
- `/api/users`
- `/api/knowledge-bases`
- `/api/documents`
- `/api/chat`
- `/api/agent`
- `/api/usage`
- `/api/feedback`

## 安全要求

- API Key 不进前端
- 用户数据隔离
- 向量检索带权限过滤
- 上传文件限制类型和大小
- 日志脱敏
- 高风险 Agent 工具人工确认

## 验收标准

- [ ] 能部署运行
- [ ] 能登录
- [ ] 能创建知识库
- [ ] 能上传文档
- [ ] 能完成 RAG 问答
- [ ] 能展示引用来源
- [ ] 能保存聊天记录
- [ ] 能统计 Token
- [ ] 能限制用户访问自己的知识库
- [ ] 能用 Docker Compose 启动

## 简历描述

```text
基于 Vue3、FastAPI、PostgreSQL、Qdrant 和大模型 API 实现企业级知识库智能客服系统。
系统支持文档上传、PDF 解析、文本切分、Embedding 向量化、语义检索、RAG 问答、引用来源、流式输出、用户权限、Token 用量统计、Agent 工具调用和 Docker 部署。
```

