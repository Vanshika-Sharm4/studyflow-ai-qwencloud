# StudyFlow AI

StudyFlow AI is an AI-powered study assistant built for the QwenCloud Hackathon.

## Track

Autopilot Agent

## What it does

StudyFlow AI helps students turn messy class notes into organized study material.

Users can paste their course notes, and the app generates:

- A clear summary
- Important key terms
- Practice quiz questions with answers
- A simple study plan

## Why I built it

Students often have long notes, lecture material, or copied textbook information but do not always know how to turn that material into useful study resources. StudyFlow AI helps automate that workflow.

## How it uses QwenCloud

The backend uses the QwenCloud OpenAI-compatible API to send the student's notes to a Qwen model and generate structured study material.

The API key is stored locally in a `.env` file and is not included in this repository.

## Tech Stack

- Python
- Flask
- Flask-CORS
- QwenCloud API
- OpenAI Python SDK
- HTML
- JavaScript
- GitHub
- Alibaba Cloud for deployment

## Project Structure

```text
qwencloud-hackathon/
├── backend/
│   ├── app.py
│   ├── qwen_client.py
│   └── requirements.txt
├── frontend/
│   └── index.html
├── docs/
├── .gitignore
├── LICENSE
└── README.md
