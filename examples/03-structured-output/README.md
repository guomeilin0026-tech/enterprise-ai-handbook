# 示例 03：结构化输出

目标：让 AI 返回前端能直接渲染的数据，而不是一大段散文。

## 普通输出的问题

```text
这个简历还不错，大概 80 分，优势是 Vue3，问题是后端少一点...
```

这种内容前端不好拆。

## 推荐输出

```json
{
  "score": 80,
  "strengths": ["Vue3 项目经验", "组件化能力"],
  "weaknesses": ["后端经验不足"],
  "suggestions": ["补充 FastAPI 项目经验"]
}
```

## 后端校验思路

```python
from pydantic import BaseModel


class ResumeAnalysis(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]
```

## 运行方式

```bash
pip install pydantic
python main.py
```

## 你要理解

- 企业系统需要稳定格式
- AI 输出必须校验
- 校验失败要重试或提示用户
