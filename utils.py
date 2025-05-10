import google.generativeai as genai
import re
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Replace with your key

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_quiz_questions(book_title):
    prompt = f"""
Generate 5 multiple-choice quiz questions from the book "{book_title}".
Each question should include:
- A question
- Four options labeled A, B, C, D — each on its own line, with the label followed by a period and a space (e.g., A. Option text)
- A final line like: Answer: A

Example format:

Q1: Why is habit stacking effective?  
A. It removes willpower entirely  
B. It builds on existing routines  
C. It uses peer pressure  
D. It requires external motivation  
Answer: B

Please use the same format for all 5 questions.
"""

    response = model.generate_content(prompt)

    try:
        return parse_quiz(response.text)
    except Exception as e:
        print("Parsing error:", e)
        return []

def parse_quiz(raw_text):
    questions = []
    raw_qs = re.split(r"Q\d+:\s*", raw_text.strip())[1:]  # Skip before Q1

    for block in raw_qs:
        lines = block.strip().splitlines()
        question = lines[0].strip()
        options = {}
        answer = None

        for line in lines[1:]:
            opt_match = re.match(r"([ABCD])\.\s+(.*)", line)
            if opt_match:
                key = opt_match.group(1)
                value = opt_match.group(2).strip()
                if value:  # only keep non-empty options
                    options[key] = value
            elif line.startswith("Answer:"):
                ans_match = re.match(r"Answer:\s*([ABCD])", line)
                if ans_match:
                    answer = ans_match.group(1)

        if question and options and answer:
            questions.append({
                "question": question,
                "options": options,
                "answer": answer
            })

    return questions

