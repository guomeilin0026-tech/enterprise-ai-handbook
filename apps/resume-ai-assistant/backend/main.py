from json import JSONDecodeError

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from app.llm import analyze_resume
from app.schemas import ResumeAnalysis, ResumeAnalyzeRequest

app = FastAPI(title="AI Resume Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/resume/analyze", response_model=ResumeAnalysis)
async def analyze(request: ResumeAnalyzeRequest):
    try:
        return await analyze_resume(request.resume, request.job_description)
    except JSONDecodeError as exc:
        raise HTTPException(status_code=502, detail="模型没有返回合法 JSON") from exc
    except ValidationError as exc:
        raise HTTPException(status_code=502, detail="模型返回结构不符合要求") from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="简历分析失败") from exc

