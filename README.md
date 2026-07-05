# 企业 AI 应用全栈学习仓库

这是一套面向初学者的企业 AI 应用开发学习仓库。

目标不是训练大模型，而是学会把大模型真正接入业务系统，做出可以演示、可以部署、可以写进简历的企业 AI 应用。

## 当前版本

当前仓库是：

```text
教学版学习仓库
```

适合：

- 学习
- 练习
- 作品集
- 面试准备
- 企业 AI 项目原型参考

不建议直接作为生产级商业系统使用。

如果要升级生产级，请看：

- [docs/当前版本说明.md](./docs/当前版本说明.md)
- [docs/生产级升级路线.md](./docs/生产级升级路线.md)

## 适合谁

- 会一点前端，尤其是 Vue3
- 后端基础较弱，想用 Python FastAPI 入门
- 想学习大模型应用开发
- 想做 RAG 知识库、Agent、智能客服、企业 AI 工具
- 想把 AI 项目作为作品集或求职项目

## 你会学到什么

```text
大模型基础
Prompt Engineering
Structured Output
Function Calling
MCP
Agent
Workflow
RAG 企业知识库
多模态
企业 AI 工程化
Docker 部署
企业数据安全
AI 产品思维
面试与架构设计
```

## 推荐技术栈

```text
前端：Vue3 + TypeScript
后端：Python + FastAPI
数据库：PostgreSQL
向量数据库：Qdrant
大模型：OpenAI-compatible API
部署：Docker + Nginx
```

## 仓库目录

```text
完整课程/                 # 16 章课程正文
examples/                 # 核心知识点最小代码示例
projects/                 # 实战项目路线
interview/                # 面试题库
docs/                     # 工程规范、部署、安全、架构说明
checklists/               # 学习打卡和项目验收清单
templates/                # README、PRD、架构设计模板
assets/                   # 架构图源码和图片资源
answers/                  # 作业参考答案
instructor/               # 课程设计规范和讲师手册
apps/                     # 完整实战项目源码入口
presentations/            # 项目讲解稿
troubleshooting/           # 常见报错和排查
.github/workflows/        # GitHub Actions CI
CONTRIBUTING.md           # 贡献指南
CHANGELOG.md              # 更新日志
.env.example              # 环境变量示例
FAQ.md                    # 常见问题
企业AI全栈课程大纲.md      # 课程总大纲
学习路线.md               # 建议学习顺序
新手入门指南.md            # 从 0 开始怎么学
README.md                 # 仓库入口
```

## 从哪里开始

如果你是小白，按这个顺序：

1. 先看 [新手入门指南.md](./新手入门指南.md)
2. 再看 [学习路线.md](./学习路线.md)
3. 然后进入 [完整课程](./完整课程/README.md)
4. 看 [examples](./examples/README.md) 跑最小示例
5. 按 [projects](./projects/README.md) 完成实战项目
6. 进入 [apps](./apps/README.md) 跑完整项目源码
7. 用 [每日学习计划](./checklists/每日学习计划.md) 和 [checklists](./checklists/README.md) 做打卡验收
8. 用 [answers](./answers/README.md) 对照作业答案
9. 用 [presentations](./presentations/README.md) 练习项目讲解
10. 用 [interview](./interview/README.md) 准备面试
11. 遇到问题看 [FAQ.md](./FAQ.md) 和 [常见报错](./troubleshooting/常见报错.md)
12. 发布前看 [发布前检查清单](./checklists/发布前检查清单.md)

## 运行示例前安装依赖

```bash
pip install -r requirements.txt
```

复制环境变量示例：

```bash
cp .env.example .env
```

## 课程目录

- [第01章：AI 行业全景（2026）](./完整课程/第01章-AI行业全景2026.md)
- [第02章：大模型基础（LLM）](./完整课程/第02章-大模型基础LLM.md)
- [第03章：Prompt Engineering（企业级）](./完整课程/第03章-PromptEngineering企业级.md)
- [第04章：Function Calling](./完整课程/第04章-FunctionCalling.md)
- [第05章：Structured Output](./完整课程/第05章-StructuredOutput.md)
- [第06章：MCP（最详细）](./完整课程/第06章-MCP最详细.md)
- [第07章：Agent（最详细）](./完整课程/第07章-Agent最详细.md)
- [第08章：Workflow（Dify、n8n）](./完整课程/第08章-Workflow-Dify-n8n.md)
- [第09章：RAG（企业知识库）](./完整课程/第09章-RAG企业知识库.md)
- [第10章：多模态（OCR、图片、视频）](./完整课程/第10章-多模态OCR图片视频.md)
- [第11章：企业 AI 工程化](./完整课程/第11章-企业AI工程化.md)
- [第12章：Docker 部署](./完整课程/第12章-Docker部署.md)
- [第13章：企业数据安全](./完整课程/第13章-企业数据安全.md)
- [第14章：企业项目案例（10+）](./完整课程/第14章-企业项目案例10个.md)
- [第15章：AI 产品经理思维](./完整课程/第15章-AI产品经理思维.md)
- [第16章：面试与架构设计](./完整课程/第16章-面试与架构设计.md)

## 最终项目目标

学完后，你应该能做出：

```text
企业知识库 + 智能客服系统
```

核心功能：

- 文档上传
- 文档解析
- 文本切分
- Embedding 向量化
- 向量检索
- RAG 问答
- 引用来源
- 流式输出
- 用户权限
- Token 用量统计
- Docker 部署

## 学习建议

- 不要只看概念，每章都要做练习。
- 不要一开始学模型训练，先学会做 AI 应用。
- 不要把 API Key 放到前端或 GitHub。
- 不要追求一次学完，按阶段推进。
- 学到 RAG 和 Agent 时，一定要做项目。

## 完整学习闭环

```text
学习路线.md
-> 完整课程/
-> examples/
-> projects/
-> apps/
-> docs/
-> checklists/
-> answers/
-> presentations/
-> interview/
-> troubleshooting/
```

每个阶段都要做到：

```text
能理解
能写代码
能做项目
能讲清楚
能通过验收清单
```

## 当前状态

这个仓库目前已经包含完整 16 章主线内容、学习路线、示例目录、项目路线、工程规范、检查清单、文档模板、面试题库，以及四个完整实战项目：`apps/ai-chat-assistant`、`apps/resume-ai-assistant`、`apps/personal-rag-knowledge-base`、`apps/enterprise-ai-customer-service`。

后续可以继续补充：

```text
更多可运行代码示例
企业级项目的 PostgreSQL + Qdrant 升级版
```
