import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen3.7-plus",
    messages=[
        {
            "role": "user",
            "content": "Give me one simple hackathon project idea using AI agents."
        }
    ],
)

print(completion.choices[0].message.content)