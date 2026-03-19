# AI Resume Analyzer

An AI-powered backend service that analyzes resumes and returns targeted evaluation reports and improvement suggestions using OpenAI GPT API.

## Tech Stack

- **Backend:** Python, FastAPI
- **AI:** OpenAI GPT API, Prompt Engineering
- **Database:** PostgreSQL
- **Infrastructure:** Docker, AWS EC2

## Features

- Resume upload and parsing
- AI-generated evaluation reports with structured feedback
- Async analysis job queuing and result retrieval
- User session and analysis history persistence
- Input validation and fallback error-handling for stable LLM output processing

## Architecture
```
Client → FastAPI → OpenAI GPT API
                ↓
          PostgreSQL (session & history storage)
```

## Getting Started
```bash
git clone https://github.com/annieleen23/ai-resume-analyzer.git
cd ai-resume-analyzer
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload resume for analysis |
| GET | `/result/{job_id}` | Retrieve analysis result |
| GET | `/history` | Get user analysis history |

## Deployment

Containerized with Docker and deployed to AWS EC2.
