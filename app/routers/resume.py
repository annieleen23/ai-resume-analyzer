from fastapi import APIRouter, HTTPException
from app.models.resume import ResumeAnalysisRequest, AnalysisJob
from app.services.analyzer import create_analysis_job, get_job

router = APIRouter(prefix="/api/v1", tags=["resume"])


@router.post("/analyze", response_model=dict)
async def analyze_resume(request: ResumeAnalysisRequest):
    if not request.resume_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty")
    if len(request.resume_text) > 10000:
        raise HTTPException(status_code=400, detail="Resume text too long (max 10000 chars)")
    job_id = create_analysis_job(request.resume_text, request.job_description)
    return {"job_id": job_id, "status": "pending", "message": "Analysis started"}


@router.get("/results/{job_id}", response_model=AnalysisJob)
async def get_results(job_id: str):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI Resume Analyzer"}
