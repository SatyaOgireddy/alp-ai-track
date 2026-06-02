import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# Ask user for topic
topic = input("Enter topic: ")

# Prompt for Gemini
prompt = f"""
Generate:
1. Five MCQs
2. Two short-answer questions
3. One programming question
4. Provide answers

Topic: {topic}
"""

# Send request
response = model.generate_content(prompt)

# Display output
print("\nGenerated Questions:\n")
print(response.text)