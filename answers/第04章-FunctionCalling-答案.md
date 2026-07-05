# 第 4 章：Function Calling 参考答案

## Function Calling 是什么

参考答案：

```text
Function Calling 是让模型根据用户意图选择需要调用的函数，并生成函数参数。真正执行函数的是后端，不是模型本身。
```

## 工具参数为什么要校验

参考答案：

```text
因为模型生成的参数可能错误、缺失或被用户恶意诱导。后端必须校验参数格式和权限，不能直接相信模型输出。
```

## 查订单工具设计

```json
{
  "name": "get_order_status",
  "arguments": {
    "order_id": "10086"
  },
  "result": {
    "status": "已发货",
    "estimate_time": "明天送达"
  }
}
```

