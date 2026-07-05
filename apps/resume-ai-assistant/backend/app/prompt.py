def build_resume_prompt(resume: str, job_description: str) -> str:
    return f"""
你是一名资深 HR 和职业发展顾问。

请根据【候选人简历】和【岗位 JD】进行分析。

要求：
1. 输出必须是 JSON。
2. 不要输出 Markdown。
3. 不要输出 JSON 之外的解释。
4. score 是 0 到 100 的整数。
5. strengths、weaknesses、suggestions、interview_questions 必须是字符串数组。

JSON 格式：
{{
  "score": 85,
  "strengths": ["优势 1", "优势 2"],
  "weaknesses": ["不足 1", "不足 2"],
  "suggestions": ["建议 1", "建议 2"],
  "rewritten_summary": "优化后的个人总结",
  "interview_questions": ["面试问题 1", "面试问题 2"]
}}

【候选人简历】
{resume}

【岗位 JD】
{job_description}
""".strip()

