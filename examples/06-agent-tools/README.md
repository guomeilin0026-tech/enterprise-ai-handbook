# 示例 06：Agent 工具调用

目标：理解 Agent 如何通过工具完成任务。

## 普通 AI 和 Agent 的区别

普通 AI：

```text
用户：查订单 10086
AI：我无法查询订单。
```

Agent：

```text
用户：查订单 10086
AI：需要调用订单查询工具
后端：执行 get_order_status("10086")
AI：订单已发货，预计明天送达
```

## 工具函数示例

```python
def get_order_status(order_id: str):
    return {
        "order_id": order_id,
        "status": "已发货",
        "estimate_time": "明天送达"
    }
```

## 工具调用结果

```json
{
  "tool": "get_order_status",
  "arguments": {
    "order_id": "10086"
  }
}
```

## 运行方式

```bash
python main.py
```

这个示例先用规则模拟 Agent。真实项目里：

```text
模型负责判断调用哪个工具
后端负责执行工具
```

## 你要理解

- AI 不是真的自己查数据库
- AI 负责判断调用哪个工具
- 后端负责执行工具
- 工具参数必须校验
- 高风险工具必须人工确认
