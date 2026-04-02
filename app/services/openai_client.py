import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume_with_gpt(resume_text: str, job_description: str = None) -> dict:
    job_context = ""
    if job_description:
        job_context = f"\n\nJob Description to match against:\n{job_description}"

    prompt = f"""You are an expert technical recruiter with 10 years of experience evaluating software engineering resumes.

Analyze the following resume and provide structured feedback.{job_context}

Resume:
{resume_text}

Respond ONLY with a valid JSON object in exactly this format, no additional text:
{{
    "overall_score": <integer 1-100>,
    "strengths": ["<strength 1>", "<strength 2>", "<strength 3>"],
    "weaknesses": ["<weakness 1>", "<weakness 2>"],
    "suggestions": ["<actionable suggestion 1>", "<actionable suggestion 2>", "<actionable suggestion 3>"],
    "keyword_match": ["<matched keyword 1>", "<matched keyword 2>"],
    "missing_keywords": ["<missing keyword 1>", "<missing keyword 2>"]
}}"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert resume reviewer. Always respond with valid JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1000,
    )

    raw = response.choices[0].message.content.strip()
    return json.loads(raw)
