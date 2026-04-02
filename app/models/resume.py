from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class ResumeAnalysisRequest(BaseModel):
    resume_text: str
    job_description: Optional[str] = None


class AnalysisResult(BaseModel):
    overall_score: int
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    keyword_match: List[str]
    missing_keywords: List[str]


class AnalysisJob(BaseModel):
    job_id: str
    status: JobStatus
    result: Optional[AnalysisResult] = None
    error: Optional[str] = None
