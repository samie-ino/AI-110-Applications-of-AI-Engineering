import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def verify(problem, diagnosis):
    prompt = f"""
You are an evaluator checking an AI-generated diagnosis.

Problem:
{problem}

Diagnosis:
{diagnosis}

Do the following:
1. Check if the reasoning is correct
2. Identify any issues
3. Give a confidence score

Return format:
Issues: ...
Confidence: X%
"""

    try:
        response = model.generate_content(prompt)
        result = response.text

        confidence = "Unknown"
        for line in result.split("\n"):
            if "Confidence" in line:
                confidence = line.strip()

        return result, confidence

    except Exception as e:
        return f"Error verifying: {e}", "Error"
