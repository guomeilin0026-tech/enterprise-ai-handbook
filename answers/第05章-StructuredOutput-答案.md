# 第 5 章：Structured Output 参考答案

## 为什么需要结构化输出

参考答案：

```text
企业系统需要把 AI 结果渲染成卡片、表格、标签或表单。如果 AI 只输出一大段文字，前端难以稳定解析。结构化输出可以让后端校验、前端直接渲染。
```

## 简历分析 JSON 示例

```json
{
  "score": 82,
  "strengths": ["Vue3 基础好", "项目经历清晰"],
  "weaknesses": ["后端经验不足"],
  "suggestions": ["补充 FastAPI 和 RAG 项目"],
  "rewritten_summary": "具备 Vue3 前端基础，正在向企业 AI 应用全栈方向发展。"
}
```

