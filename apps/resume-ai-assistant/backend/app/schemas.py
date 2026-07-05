from pydantic import BaseModel, Field


class ResumeAnalyzeRequest(BaseModel):
    resume: str = Field(..., min_length=10)
    job_description: str = Field(..., min_length=10)


class ResumeAnalysis(BaseModel):
    score: int = Field(..., ge=0, le=100)
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]
    rewritten_summary: str
    interview_questions: list[str]

