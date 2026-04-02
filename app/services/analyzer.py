import uuid
import threading
from typing import Dict
from app.models.resume import AnalysisJob, AnalysisResult, JobStatus
from app.services.openai_client import analyze_resume_with_gpt

jobs: Dict[str, AnalysisJob] = {}


def create_analysis_job(resume_text: str, job_description: str = None) -> str:
    job_id = str(uuid.uuid4())
    jobs[job_id] = AnalysisJob(job_id=job_id, status=JobStatus.PENDING)
    thread = threading.Thread(
        target=_run_analysis,
        args=(job_id, resume_text, job_description)
    )
    thread.daemon = True
    thread.start()
    return job_id


def get_job(job_id: str) -> AnalysisJob:
    return jobs.get(job_id)


def _run_analysis(job_id: str, resume_text: str, job_description: str = None):
    jobs[job_id].status = JobStatus.PROCESSING
    try:
        raw = analyze_resume_with_gpt(resume_text, job_description)
        jobs[job_id].result = AnalysisResult(**raw)
        jobs[job_id].status = JobStatus.COMPLETED
    except Exception as e:
        jobs[job_id].status = JobStatus.FAILED
        jobs[job_id].error = str(e)
