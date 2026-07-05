# 示例 01：最小大模型聊天

目标：理解一个 AI 聊天应用最小需要哪些部分。

## 核心流程

```text
用户输入问题
-> 后端接收问题
-> 后端调用大模型 API
-> 大模型返回回答
-> 后端返回给前端
```

## 最小后端伪代码

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    # 这里以后替换成真实大模型 API 调用
    return {
        "reply": "AI 收到了你的问题：" + request.message
    }
```

## 运行方式

进入本目录：

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

打开：

```text
http://127.0.0.1:8000/docs
```

## 你要理解

- API Key 不能放前端
- 前端只请求自己的后端
- 后端负责调用大模型
- 返回给前端的最好是稳定 JSON
