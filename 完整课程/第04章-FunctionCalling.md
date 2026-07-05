# 第 4 章：Function Calling

## 4.1 Function Calling 是什么

Function Calling 是让模型决定是否调用你提供的函数。

模型不会真的执行函数，真正执行的是你的后端。

流程：

```text
用户提问
-> 模型判断需要工具
-> 模型返回工具名和参数
-> 后端执行函数
-> 函数结果返回给模型
-> 模型生成最终回答
```

## 4.2 为什么需要 Function Calling

普通大模型不能直接查订单、查数据库、发邮件。

但你可以给它工具：

```text
get_order_status(order_id)
get_user_info(user_id)
send_email(to, subject, content)
```

这样模型就能通过后端间接完成真实操作。

## 4.3 工具设计原则

工具名要清楚：

```text
好的：get_order_status
差的：tool1
```

参数要明确：

```json
{
  "order_id": "10086"
}
```

返回结果要结构化：

```json
{
  "order_id": "10086",
  "status": "已发货",
  "estimate_time": "明天送达"
}
```

## 4.4 后端职责

后端必须做：

- 校验工具参数
- 判断用户有没有权限
- 执行真实函数
- 记录工具调用日志
- 处理工具失败
- 把结果返回给模型

## 4.5 典型案例：查订单

用户：

```text
帮我查订单 10086 到哪了
```

模型判断：

```json
{
  "tool": "get_order_status",
  "arguments": {
    "order_id": "10086"
  }
}
```

后端执行工具后返回：

```json
{
  "status": "已发货",
  "delivery_time": "明天送达"
}
```

最终回答：

```text
订单 10086 已发货，预计明天送达。
```

## 本章练习

- [ ] 设计一个查订单工具
- [ ] 设计一个查用户工具
- [ ] 写出每个工具的参数和返回值
- [ ] 说明工具调用为什么要做权限校验

