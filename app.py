import streamlit as st
from utils import generate_quiz_questions

st.title("📚 BookWise")
st.subheader("LLM-powered quiz app for remembering what you read")

books = [
    "Atomic Habits by James Clear",
    "Deep Work by Cal Newport",
    "Sapiens by Yuval Noah Harari",
    "Thinking, Fast and Slow by Daniel Kahneman",
    "The Power of Now by Eckhart Tolle",
    "The Subtle Art of Not Giving a F*ck by Mark Manson",
    "The 7 Habits of Highly Effective People by Stephen Covey",
    "Educated by Tara Westover",
    "Becoming by Michelle Obama",
    "The Alchemist by Paulo Coelho",
    "The Four-Hour Workweek by Tim Ferriss",
    "Outliers by Malcolm Gladwell",
    "The Lean Startup by Eric Ries",
    "Start with Why by Simon Sinek",
    "Grit by Angela Duckworth",
    "The Millionaire Next Door by Thomas Stanley",
    "Dare to Lead by Brené Brown",
    "The Art of Happiness by Dalai Lama",
    "Principles by Ray Dalio",
    "How to Win Friends and Influence People by Dale Carnegie",
    "Quiet: The Power of Introverts by Susan Cain",
    "The Intelligent Investor by Benjamin Graham",
    "Range: Why Generalists Triumph in a Specialized World by David Epstein",
    "The Power of Habit by Charles Duhigg",
    "The 48 Laws of Power by Robert Greene",
    "Good to Great by Jim Collins",
    "The Psychology of Money by Morgan Housel",
    "Man's Search for Meaning by Viktor Frankl",
    "Shoe Dog by Phil Knight",
    "Atomic Habits by James Clear",
    "The Road Less Traveled by M. Scott Peck",
    "The Secret by Rhonda Byrne",
    "Meditations by Marcus Aurelius",
    "The Untethered Soul by Michael A. Singer",
    "The E-Myth Revisited by Michael E. Gerber",
    "The Art of War by Sun Tzu",
    "Drive: The Surprising Truth About What Motivates Us by Daniel Pink",
    "The Magic of Thinking Big by David Schwartz",
    "The Compound Effect by Darren Hardy",
    "How to Stop Worrying and Start Living by Dale Carnegie",
    "The Art of Thinking Clearly by Rolf Dobelli",
    "The Happiness Project by Gretchen Rubin",
    "When Breath Becomes Air by Paul Kalanithi",
    "The Book Thief by Markus Zusak",
    "Rich Dad Poor Dad by Robert Kiyosaki",
    "Zero to One by Peter Thiel",
    "Principles: Life and Work by Ray Dalio",
    "Blink: The Power of Thinking Without Thinking by Malcolm Gladwell",
    "The Science of Getting Rich by Wallace D. Wattles",
    "The Power of Now by Eckhart Tolle",
    "The 10X Rule by Grant Cardone",
    "The War of Art by Steven Pressfield",
    "The Art of Asking by Amanda Palmer",
    "You Are a Badass by Jen Sincero",
    "The Magic of Believing by Claude M. Bristol",
    "Make Your Bed by Admiral William H. McRaven",
    "The Gifts of Imperfection by Brené Brown"
]

selected_book = st.selectbox("Select a book you've read:", books)

if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if st.button("Generate Quiz"):
    with st.spinner("Generating quiz..."):
        st.session_state.questions = generate_quiz_questions(selected_book)
        st.session_state.answers = {}
        st.session_state.submitted = False

if st.session_state.questions:
    st.markdown("### Quiz Questions")

    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"**Q{i+1}: {q['question']}**")
        selected = st.radio(
            label="Your answer:",
            options=list(q['options'].values()),  # Show only option texts
            key=f"q{i}",
            index=None  # No default selected
        )
        st.session_state.answers[i] = selected
        st.markdown("---")

    if st.button("Submit Quiz"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        score = 0
        st.markdown("## ✅ Quiz Results")

        for i, q in enumerate(st.session_state.questions):
            user_ans_text = st.session_state.answers.get(i)
            correct_key = q['answer']
            correct_text = q['options'].get(correct_key)

            st.markdown(f"**Q{i+1}: {q['question']}**")
            st.markdown(f"- Your answer: **{user_ans_text or 'No answer'}**")
            st.markdown(f"- Correct answer: **{correct_text}**")

            if user_ans_text == correct_text:
                score += 1
            st.markdown("---")

        percent = (score / len(st.session_state.questions)) * 100
        st.success(f"🎯 Your Score: {score}/5 ({percent:.0f}%)")