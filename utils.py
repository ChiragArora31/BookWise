import google.generativeai as genai
import re

genai.configure(api_key="AIzaSyACP25-MjQ2_EVbRPL-kb89uXPP0TQncLg")
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
    raw_qs = re.split(r"Q\d+:\s*", raw_text.strip())[1:]  # Skip header, split questions

    for block in raw_qs:
        lines = block.strip().splitlines()
        question = lines[0].strip()
        options = {}
        for line in lines[1:5]:
            if re.match(r"[ABCD]\.\s", line):
                key = line[0]
                value = line[3:].strip()
                options[key] = value
        answer_match = re.search(r"Answer:\s*([ABCD])", block)
        answer = answer_match.group(1).strip() if answer_match else "A"

        questions.append({
            "question": question,
            "options": options,
            "answer": answer
        })
        print(questions)
    return questions
