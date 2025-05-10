# BookWise📚🧠

Welcome to **BookWise** – your go-to web app for interactive book-based quizzes! With **BookWise**, you can dive deeper into your favorite books by testing your knowledge through fun and dynamic multiple-choice questions (MCQs). Powered by **Large Language Models (LLMs)**, this app generates questions on the fly, ensuring a fresh and challenging experience every time.

## Key Features
- **Dynamic MCQ Generation**: Using advanced language models, BookWise automatically generates 5 engaging multiple-choice questions based on the content of popular books.
- **Instant Feedback**: Receive immediate feedback on your answers with a real-time score displayed at the end of the quiz.
- **Visually Appealing UI**: Designed with user experience in mind, BookWise offers a sleek, modern, and engaging interface to keep you immersed in your quiz experience.

## Technical Working Behind the Scenes
BookWise uses a **Large Language Model (LLM)**, which processes the text of books and generates relevant multiple-choice questions. The app's architecture consists of:
1. **Text Generation**: The LLM analyzes a book's content and generates questions based on key topics, characters, themes, and plot points.
2. **Question Formatting**: The generated questions are then formatted into a multiple-choice style with one correct answer and several distractors.
3. **Streamlit Interface**: The app utilizes **Streamlit** to deliver a smooth, interactive quiz-taking experience. It allows users to select a book, take the quiz, and receive a score in a user-friendly layout.

## Requirements
- **Python 3.x**
- Streamlit
- Requests (for API calls, if applicable)
- BeautifulSoup4 (for web scraping or parsing, if required)

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ChiragArora31/BookWise
