# 第 6 章：MCP 参考答案

## 1. MCP 是什么

参考答案：

```text
MCP 是 AI 应用连接外部工具和资源的一套标准协议。它让 AI 应用可以用统一方式发现和使用文件、数据库、GitHub、企业系统等外部能力。
```

## 2. MCP 解决了什么问题

参考答案：

```text
它解决了 AI 应用接入外部工具方式不统一的问题。没有 MCP 时，每个工具都要单独适配。有 MCP 后，工具、资源、Prompt 模板可以用标准方式暴露给 AI 应用。
```

## 3. MCP 和 Function Calling 的区别

参考答案：

```text
Function Calling 更关注模型一次调用中如何选择函数和生成参数。MCP 更关注外部工具和资源如何以标准协议提供给 AI 应用。二者可以一起使用：Agent 用 Function Calling 决定工具，工具能力由 MCP Server 提供。
```

## 4. 企业知识库 MCP Server 设计

参考工具：

```text
search_knowledge_base：搜索知识库片段
get_document_detail：读取文档详情
list_knowledge_bases：列出用户可访问的知识库
```

权限要求：

```text
所有工具都必须校验 user_id 或 tenant_id，防止用户访问没有权限的知识库。
```

