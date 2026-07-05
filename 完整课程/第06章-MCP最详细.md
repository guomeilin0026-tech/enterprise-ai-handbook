# 第 6 章：MCP（最详细）

## 本章目标

学完本章，你要能回答：

- MCP 是什么
- MCP 解决什么问题
- MCP 和 Function Calling 有什么区别
- MCP 和 Agent 是什么关系
- 企业为什么会需要 MCP
- 如何设计一个企业内部 MCP Server

## 6.1 MCP 是什么

MCP 可以理解成：

```text
AI 应用连接外部工具和数据资源的一套标准协议。
```

小白理解：

```text
大模型本身只会理解和生成文本。
如果它想读取文件、查数据库、访问 GitHub、调用企业系统，就需要外部工具。
MCP 就是把这些外部工具用统一方式提供给 AI。
```

## 6.2 为什么需要 MCP

没有 MCP 时，每个 AI 应用都要自己设计工具接入方式：

```text
这个系统一套工具格式
那个系统一套工具格式
每接一个工具都要重新适配
```

有 MCP 后，可以统一描述：

- 有哪些工具
- 工具需要什么参数
- 工具返回什么结果
- 有哪些资源可以读取
- 有哪些 Prompt 模板可以复用

你可以把 MCP 理解成：

```text
AI 工具生态的 USB 接口。
```

不是每个设备都重新设计插口，而是使用统一连接方式。

## 6.3 MCP 的核心角色

### MCP Client

使用工具的一方。

通常是：

- AI IDE
- AI 助手
- Agent 系统
- 大模型应用后端

### MCP Server

提供工具和资源的一方。

例如：

- 文件系统 MCP Server
- 数据库 MCP Server
- GitHub MCP Server
- 企业 CRM MCP Server
- 企业知识库 MCP Server

### Tools

可以执行的动作。

例如：

```text
读取文件
查询数据库
创建工单
搜索知识库
获取订单状态
```

### Resources

可以读取的数据资源。

例如：

```text
某个文件
某个数据库表结构
某份项目文档
某个知识库目录
```

### Prompts

预置 Prompt 模板。

例如：

```text
代码审查 Prompt
合同审查 Prompt
知识库问答 Prompt
工单分类 Prompt
```

## 6.4 MCP 工作流程

```text
AI 应用启动
-> 连接 MCP Server
-> 获取工具和资源列表
-> 用户提出任务
-> AI 判断需要哪个工具
-> 调用 MCP Server 的工具
-> MCP Server 执行并返回结果
-> AI 基于结果继续回答
```

## 6.5 MCP 和 Function Calling 的区别

Function Calling 更关注：

```text
模型这一次调用中，如何描述函数、选择函数、生成参数。
```

MCP 更关注：

```text
工具和资源如何标准化地暴露给 AI 应用。
```

对比：

```text
Function Calling：一次模型调用里的工具调用机制
MCP：AI 应用和外部工具之间的标准连接协议
```

它们不是互斥关系。

实际系统中可以是：

```text
Agent 使用 Function Calling 决定要调用工具
工具能力由 MCP Server 提供
```

## 6.6 MCP 和 Agent 的关系

Agent 负责：

- 理解任务
- 判断下一步
- 选择工具
- 组织结果

MCP 负责：

- 提供工具
- 提供资源
- 统一工具接入方式

一句话：

```text
Agent 是大脑，MCP 是工具接口。
```

## 6.7 企业 MCP 场景

### 数据库 MCP Server

能力：

- 查看表结构
- 查询业务数据
- 生成安全 SQL

注意：

- 必须限制权限
- 不能让 AI 随意执行删除或更新

### 知识库 MCP Server

能力：

- 搜索企业文档
- 读取知识库目录
- 获取文档片段

适合：

- 内部问答
- 客服助手
- 研发知识库

### 工单 MCP Server

能力：

- 查询工单
- 创建工单
- 更新工单状态

高风险操作要人工确认。

### GitHub MCP Server

能力：

- 查询 Issue
- 查询 PR
- 读取代码
- 生成变更摘要

## 6.8 设计企业 MCP Server 的步骤

1. 确定业务系统
2. 列出可暴露的工具
3. 给每个工具设计参数
4. 给每个工具设计返回值
5. 加权限控制
6. 加日志审计
7. 给高风险工具加人工确认

## 6.9 工具设计示例

工具名：

```text
search_company_knowledge
```

用途：

```text
搜索企业知识库资料
```

参数：

```json
{
  "query": "年假怎么算",
  "knowledge_base_id": "kb_001",
  "top_k": 5
}
```

返回：

```json
{
  "results": [
    {
      "document_name": "员工手册.pdf",
      "content": "员工入职满一年后可享受年假...",
      "score": 0.89
    }
  ]
}
```

## 6.10 常见坑

### 坑 1：把 MCP 当成模型

MCP 不是模型，它是连接工具和资源的协议。

### 坑 2：工具权限过大

不要让 AI 拥有数据库管理员权限。

### 坑 3：没有日志

企业必须知道 AI 调用了什么工具、传了什么参数、返回了什么结果。

### 坑 4：高风险操作自动执行

删除数据、发邮件、付款、审批这类操作必须人工确认。

## 本章实战任务

- [ ] 画出 MCP Client 和 MCP Server 的关系图
- [ ] 设计一个企业知识库 MCP Server
- [ ] 为它设计 3 个工具
- [ ] 写出每个工具的参数和返回值
- [ ] 标出哪些工具需要权限控制

## 本章面试题

1. MCP 是什么？
2. MCP 解决了什么问题？
3. MCP 和 Function Calling 有什么区别？
4. MCP 和 Agent 是什么关系？
5. 企业内部 MCP Server 为什么必须做权限控制？

## 本章总结

你只需要记住：

```text
MCP 是 AI 应用连接外部工具和资源的标准协议。
Agent 可以通过 MCP 使用企业系统能力。
企业使用 MCP 时，权限、安全、日志和人工确认非常重要。
```

