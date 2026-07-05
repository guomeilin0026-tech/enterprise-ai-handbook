import json
from collections.abc import AsyncGenerator

import httpx

from app.config import settings
from app.schemas import ChatMessage


SYSTEM_PROMPT = "你是一个耐心、清晰的企业 AI 应用学习助手。回答要适合初学者。"


def _build_messages(message: str, history: list[ChatMessage]) -> list[dict[str, str]]:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(item.model_dump() for item in history[-10:])
    messages.append({"role": "user", "content": message})
    return messages


def _mock_reply(message: str) -> str:
    return (
        "这是 mock AI 回复。你刚才的问题是："
        f"{message}\n\n"
        "后端已经跑通了。下一步可以在 `.env` 里配置真实大模型 API。"
    )


async def chat_once(message: str, history: list[ChatMessage]) -> str:
    if settings.use_mock_llm or not settings.openai_api_key:
        return _mock_reply(message)

    url = f"{settings.openai_base_url.rstrip('/')}/chat/completions"
    payload = {
        "model": settings.openai_model,
        "messages": _build_messages(message, history),
        "temperature": 0.3,
    }
    headers = {"Authorization": f"Bearer {settings.openai_api_key}"}

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]


async def chat_stream(message: str, history: list[ChatMessage]) -> AsyncGenerator[str, None]:
    if settings.use_mock_llm or not settings.openai_api_key:
        reply = _mock_reply(message)
        for char in reply:
            yield char
        return

    url = f"{settings.openai_base_url.rstrip('/')}/chat/completions"
    payload = {
        "model": settings.openai_model,
        "messages": _build_messages(message, history),
        "temperature": 0.3,
        "stream": True,
    }
    headers = {"Authorization": f"Bearer {settings.openai_api_key}"}

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", url, headers=headers, json=payload) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if not line.startswith("data: "):
                    continue
                data = line.removeprefix("data: ").strip()
                if data == "[DONE]":
                    break
                try:
                    chunk = json.loads(data)
                    content = chunk["choices"][0].get("delta", {}).get("content", "")
                    if content:
                        yield content
                except (json.JSONDecodeError, KeyError, IndexError):
                    continue

