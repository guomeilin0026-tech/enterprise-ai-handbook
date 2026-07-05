# 示例 05：最小 RAG

目标：理解 RAG 的最小闭环。

## RAG 一句话解释

```text
先查资料，再让 AI 根据资料回答。
```

## 最小流程

```text
准备 3 段文本
-> 用户提问
-> 找出最相关文本
-> 把文本和问题一起发给模型
-> 模型根据文本回答
```

## 最小伪代码

```python
documents = [
    "员工入职满一年后可享受年假。",
    "报销需要提交发票和审批单。",
    "离职工资会在下一个工资日发放。"
]


def search_documents(question):
    # 真实项目里这里应该使用 Embedding + 向量数据库
    if "年假" in question:
        return documents[0]
    if "报销" in question:
        return documents[1]
    if "离职" in question:
        return documents[2]
    return ""


question = "年假怎么算？"
context = search_documents(question)

prompt = f"""
请只根据资料回答问题。

资料：
{context}

问题：
{question}
"""
```

## 运行方式

```bash
python main.py
```

这个示例先用关键词模拟检索。真实项目要替换为：

```text
Embedding + Qdrant
```

## 你要理解

- 真实 RAG 不是关键词搜索，而是语义搜索
- Embedding 用来把文本变成向量
- 向量数据库用来找语义相近的文档片段
- 引用来源能减少幻觉风险
