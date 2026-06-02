# alp-ai-track
AI Literacy and Agentic AI Programme

## Week 1: Gemini Teaching Assistant

### Description
This project uses the Google Gemini API to generate:

- 5 MCQs
- 2 Short Answer Questions
- 1 Programming Question
- Answers

based on any topic entered by the user.

### Technologies Used

- Python
- Google Gemini API
- Cursor AI
- GitHub

### How to Run

Install dependencies:

```bash
pip install google-generativeai python-dotenv
```

Create a local `.env` file with your API key (do not commit this file):

```bash
copy .env.example .env
```

Edit `.env` and set `GOOGLE_API_KEY` to your Google Gemini API key.

Run the teaching assistant:

```bash
python scripts/teaching_assistant.py
```
