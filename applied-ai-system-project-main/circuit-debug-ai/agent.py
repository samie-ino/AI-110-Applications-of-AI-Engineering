import google.generativeai as genai
import os
from dotenv import load_dotenv
from retriever import retrieve_context

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def diagnose(problem):
    context = retrieve_context(problem)

    prompt = f"""
You are a specialized electrical engineering assistant.

Follow these steps:
1. Think step-by-step about the problem
2. Use the provided context if relevant
3. Output clearly:
   - Possible causes
   - Suggested tests

Context:
{context}

Problem:
{problem}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating diagnosis: {e}"
