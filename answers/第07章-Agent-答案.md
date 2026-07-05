# 第 7 章：Agent 参考答案

## 1. Agent 是什么

参考答案：

```text
Agent 是能根据用户目标选择步骤、调用工具、读取工具结果并继续完成任务的 AI 系统。它不只是回答问题，还能通过工具完成查询、生成、创建等操作。
```

## 2. Agent 和普通聊天的区别

参考答案：

```text
普通聊天主要是用户问、AI 答。Agent 可以判断是否需要调用工具，例如查订单、查知识库、生成报表，然后根据工具结果继续回答。
```

## 3. Agent 和 RAG 的区别

参考答案：

```text
RAG 主要解决“查资料后回答”的问题。Agent 主要解决“调用工具完成任务”的问题。企业项目里经常把两者结合起来，例如 Agent 调用知识库检索工具完成问答。
```

## 4. 订单查询 Agent 工具设计

工具名：

```text
get_order_status
```

参数：

```json
{
  "order_id": "string"
}
```

返回：

```json
{
  "order_id": "10086",
  "status": "已发货",
  "estimate_time": "明天送达"
}
```

日志字段：

```text
user_id
tool_name
arguments_json
result_json
status
created_at
```

## 5. 为什么高风险工具要人工确认

参考答案：

```text
因为模型可能理解错用户意图或生成错误参数。删除数据、发邮件、付款、提交审批等操作会影响真实业务，必须由用户确认后才能执行。
```

