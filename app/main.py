from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.resume import router

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes using OpenAI GPT and return structured feedback",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "AI Resume Analyzer API", "docs": "/docs"}
