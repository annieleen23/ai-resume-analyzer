from pydantic_settings import BaseSettings

class Settings:
    app_name: str = "AI Resume Analyzer"
    max_resume_length: int = 10000
    openai_model: str = "gpt-3.5-turbo"
    max_tokens: int = 1000
    temperature: float = 0.2

settings = Settings()
