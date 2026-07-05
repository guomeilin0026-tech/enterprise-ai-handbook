# 项目 2：AI 简历优化助手

## 项目目标

掌握 Prompt Engineering 和 Structured Output。

## 用户故事

作为求职者，我希望输入简历和岗位 JD，让 AI 帮我分析匹配度并给出修改建议。

## 功能清单

- [ ] 输入简历
- [ ] 输入岗位 JD
- [ ] AI 分析匹配度
- [ ] AI 输出优势
- [ ] AI 输出不足
- [ ] AI 输出修改建议
- [ ] AI 改写简历片段
- [ ] 前端卡片展示结果

## 输出结构

```json
{
  "score": 85,
  "strengths": ["Vue3 项目经验"],
  "weaknesses": ["后端经验不足"],
  "suggestions": ["补充 FastAPI 项目"],
  "rewritten_summary": "优化后的个人总结"
}
```

## 后端要求

- 使用 Pydantic 校验 AI 输出
- JSON 解析失败时重试
- 用户输入为空时拒绝请求

## 验收标准

- [ ] AI 能输出固定 JSON
- [ ] 前端能用卡片展示
- [ ] 输出错误时后端能处理
- [ ] Prompt 可以复用

