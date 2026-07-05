from pydantic import BaseModel, ValidationError


class ResumeAnalysis(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]


mock_llm_output = {
    "score": 80,
    "strengths": ["Vue3 project experience", "Component design"],
    "weaknesses": ["Backend experience is limited"],
    "suggestions": ["Add a FastAPI AI project to the resume"],
}


try:
    result = ResumeAnalysis(**mock_llm_output)
    print(result.model_dump())
except ValidationError as error:
    print("Invalid AI output")
    print(error)

