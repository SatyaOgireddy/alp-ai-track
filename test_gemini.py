import os
from dotenv import load_dotenv
import google.generativeai as genai

print("Starting script...")

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("API Key Loaded:", api_key is not None)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

print("Sending request...")

response = model.generate_content(
    "What is Artificial Intelligence?"
)

print("Response received:")
print(response.text)