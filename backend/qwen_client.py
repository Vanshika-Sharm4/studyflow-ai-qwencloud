import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)

def generate_study_material(course_notes):
    prompt = f"""
You are StudyFlow AI, an academic study assistant.

Take the student's course notes and create:
1. A clear summary
2. Important key terms
3. 5 practice quiz questions with answers
4. A simple 3-day study plan

Course notes:
{course_notes}
"""

    completion = client.chat.completions.create(
        model="qwen3.7-plus",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return completion.choices[0].message.content