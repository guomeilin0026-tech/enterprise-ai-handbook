import json

import httpx

from app.config import settings
from app.prompt import build_resume_prompt
from app.schemas import ResumeAnalysis


def mock_analysis() -> ResumeAnalysis:
    return ResumeAnalysis(
        score=78,
        strengths=["具备 Vue3 前端基础", "有组件化开发经验", "适合向 AI 应用全栈方向转型"],
        weaknesses=["后端项目经验不足", "缺少 RAG 和 Agent 实战项目", "缺少部署和工程化经验"],
        suggestions=[
            "补充 FastAPI 后端接口项目",
            "完成一个 RAG 知识库项目",
            "在简历中突出 Vue3 + AI 应用结合能力",
        ],
        rewritten_summary=(
            "具备 Vue3 前端开发基础，正在系统学习 Python FastAPI、"
            "大模型 API、Prompt 工程和 RAG 知识库开发，目标是成为企业 AI 应用全栈工程师。"
        ),
        interview_questions=[
            "你如何理解 Vue3 前端和 FastAPI 后端在 AI 应用中的分工？",
            "为什么大模型 API Key 不能放在前端？",
            "你计划如何补齐 RAG 项目经验？",
        ],
    )


async def analyze_resume(resume: str, job_description: str) -> ResumeAnalysis:
    if settings.use_mock_llm or not settings.openai_api_key:
        return mock_analysis()

    url = f"{settings.openai_base_url.rstrip('/')}/chat/completions"
    payload = {
        "model": settings.openai_model,
        "messages": [
            {"role": "system", "content": "你只输出合法 JSON，不输出任何额外文本。"},
            {"role": "user", "content": build_resume_prompt(resume, job_description)},
        ],
        "temperature": 0.2,
    }
    headers = {"Authorization": f"Bearer {settings.openai_api_key}"}

    async with httpx.AsyncClient(timeout=90) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]

    parsed = json.loads(content)
    return ResumeAnalysis(**parsed)

