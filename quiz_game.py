import streamlit as st
import time
import random
from datetime import datetime

st.set_page_config(page_title="Quiz Game", layout="centered")

quiz_data = {
    "Computer": {
        "What does CPU stand for?": "Central Processing Unit",
        "What does GPU stand for?": "Graphics Processing Unit",
        "What does RAM stand for?": "Random Access Memory",
        "What does PSU stand for?": "Power Supply",
        "What does SSD stand for?": "Solid State Drive",
        "What is the brain of the computer?": "CPU",
        "Which key is used to refresh a webpage?": "F5",
        "What is the full form of USB?": "Universal Serial Bus",
        "What is an example of an operating system?": "Windows",
        "What does HTML stand for?": "HyperText Markup Language",
        "What is the purpose of a firewall?": "Security",
        "What device outputs hard copies?": "Printer",
        "Which part stores BIOS?": "ROM",
        "What language is used for web scripting?": "JavaScript",
        "What does LAN stand for?": "Local Area Network",
        "What is phishing?": "Scam",
        "What is malware?": "Malicious Software",
        "Which company created the iPhone?": "Apple",
        "What is the shortcut to copy?": "Ctrl+C",
        "What port is used for internet?": "Ethernet"
    },
    "Math": {
        "What is 10 + 10?": "20",
        "What is 9 x 3?": "27",
        "What is the square root of 49?": "7",
        "What is 100 divided by 4?": "25",
        "What is the area of a square with side 5?": "25",
        "What is 7 cubed?": "343",
        "Solve: 12 - 5": "7",
        "Solve: 5²": "25",
        "What is 30% of 100?": "30",
        "What is 0 divided by 10?": "0",
        "What is the value of Pi (approx)?": "3.14",
        "Is 17 a prime number?": "Yes",
        "What is 9 + 8 - 6?": "11",
        "What is 2 to the power of 4?": "16",
        "Solve: 3(4 + 2)": "18",
        "What is 144 / 12?": "12",
        "What is the perimeter of a triangle with sides 3, 4, 5?": "12",
        "What is 15% of 200?": "30",
        "What is 0.5 as a fraction?": "1/2",
        "What is 2/4 simplified?": "1/2"
    },
    "Science": {
        "What planet is known as the Red Planet?": "Mars",
        "What gas do plants absorb?": "Carbon Dioxide",
        "What is H2O?": "Water",
        "What force keeps us grounded?": "Gravity",
        "What part of the body pumps blood?": "Heart",
        "What is the boiling point of water in Celsius?": "100",
        "What is the center of an atom?": "Nucleus",
        "What is the hardest natural substance?": "Diamond",
        "What vitamin comes from sunlight?": "D",
        "What is the chemical symbol for Oxygen?": "O",
        "What do bees collect?": "Pollen",
        "What is photosynthesis?": "Food production",
        "What does DNA stand for?": "Deoxyribonucleic Acid",
        "What is the pH of water?": "7",
        "What organ helps you breathe?": "Lungs",
        "Which planet is the largest?": "Jupiter",
        "Which organ filters blood?": "Kidney",
        "What animal is the fastest?": "Cheetah",
        "What is the speed of light?": "299792458",
        "What causes tides?": "Moon"
    },
    "Geography": {
        "What is the largest ocean?": "Pacific",
        "What is the capital of France?": "Paris",
        "Which continent is Egypt in?": "Africa",
        "What river runs through Egypt?": "Nile",
        "Which is the coldest continent?": "Antarctica",
        "What is the longest river in the world?": "Nile",
        "Which country has the most population?": "China",
        "What is the capital of Japan?": "Tokyo",
        "Which country is shaped like a boot?": "Italy",
        "What ocean is between Africa and Australia?": "Indian",
        "What is the smallest continent?": "Australia",
        "Where is the Amazon rainforest?": "Brazil",
        "What desert is the largest?": "Sahara",
        "Which country is known for maple syrup?": "Canada",
        "Which U.S. state is the largest?": "Alaska",
        "What is the capital of Nigeria?": "Abuja",
        "What mountain is the highest?": "Everest",
        "What is the capital of UK?": "London",
        "What is the national animal of Australia?": "Kangaroo",
        "What sea borders Saudi Arabia?": "Red Sea"
    },
    "History": {
        "Who was the first U.S. president?": "George Washington",
        "When did World War II end?": "1945",
        "Who discovered America?": "Christopher Columbus",
        "What wall fell in 1989?": "Berlin Wall",
        "What empire did Julius Caesar belong to?": "Roman",
        "Who was the first man on the moon?": "Neil Armstrong",
        "Which war was fought from 1914 to 1918?": "World War I",
        "Who was the first female British Prime Minister?": "Margaret Thatcher",
        "Who wrote the Declaration of Independence?": "Thomas Jefferson",
        "What was the name of the ship that sank in 1912?": "Titanic",
        "Which country built the Great Wall?": "China",
        "Who was Nelson Mandela?": "President of South Africa",
        "When was the iPhone launched?": "2007",
        "Who invented the telephone?": "Alexander Graham Bell",
        "What year was the UN founded?": "1945",
        "Who painted the Mona Lisa?": "Leonardo da Vinci",
        "What was Hitler's first name?": "Adolf",
        "What was the Cold War?": "Political tension",
        "Who was Cleopatra?": "Egyptian Queen",
        "Where was Jesus born?": "Bethlehem"
    }
}

if "subject" not in st.session_state:
    st.session_state.subject = None
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "completed" not in st.session_state:
    st.session_state.completed = False
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []
if "warning" not in st.session_state:
    st.session_state.warning = False
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = []
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "time_up" not in st.session_state:
    st.session_state.time_up = False
if "timer_expired" not in st.session_state:
    st.session_state.timer_expired = False
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

TIME_LIMIT = 30 
QUESTIONS_PER_QUIZ = 5

def reset_game():
    keys = list(st.session_state.keys())
    for key in keys:
        if key not in ["quiz_data"]: 
            del st.session_state[key]

def select_random_questions(subject):
    all_questions = list(quiz_data[subject].items())
    return random.sample(all_questions, min(QUESTIONS_PER_QUIZ, len(all_questions)))

def format_time(seconds):
    return f"{int(seconds)} sec"

def is_answer_correct(user_answer, correct_answer):
    special_cases = ["ctrl+c", "f5", "ctrl + c"]
    
    user_norm = user_answer.strip().lower()
    correct_norm = correct_answer.strip().lower()
    
    if correct_norm in special_cases:
        user_clean = ''.join(filter(str.isalnum, user_norm))
        correct_clean = ''.join(filter(str.isalnum, correct_norm))
        return user_clean == correct_clean
    
    return user_norm == correct_norm

if st.session_state.subject is None:
    st.title("🎓 Quiz Game")
    st.markdown("Choose a subject to begin:")
    subject = st.selectbox("📘 Select Subject", list(quiz_data.keys()))
    if st.button("▶️ Start Quiz"):
        st.session_state.subject = subject
        st.session_state.selected_questions = select_random_questions(subject)
        st.session_state.start_time = time.time()
        st.session_state.last_update = time.time()
        st.rerun()

elif not st.session_state.completed:
    current_time = time.time()
    if current_time - st.session_state.last_update > 0.5:  
        st.session_state.last_update = current_time
        st.rerun()
    
    questions = st.session_state.selected_questions
    total = len(questions)
    q, correct_answer = questions[st.session_state.question_index]
    
    st.title(f"{st.session_state.subject} Quiz")
    st.markdown(f"**Question {st.session_state.question_index + 1} of {total}**")
    
    elapsed_time = current_time - st.session_state.start_time
    remaining_time = max(0, TIME_LIMIT - elapsed_time)
    
    timer_color = "#4CAF50"
    if remaining_time < 10:
        timer_color = "#FF5722" 
    if remaining_time < 5:
        timer_color = "#F44336" 
        
    timer_text = f"⏱️ <span style='color:{timer_color}; font-weight:bold;'>{format_time(remaining_time)}</span>"
    st.markdown(timer_text, unsafe_allow_html=True)
    
    progress_percent = remaining_time / TIME_LIMIT
    st.progress(progress_percent)
    
    if remaining_time <= 0 and not st.session_state.timer_expired:
        st.session_state.timer_expired = True
        st.session_state.time_up = True
        st.session_state.user_answers.append((q, "⏰ Time Up"))
        st.session_state.question_index += 1
        st.session_state.start_time = time.time()
        st.session_state.last_update = time.time()
        st.session_state.timer_expired = False
        
        if st.session_state.question_index >= total:
            st.session_state.completed = True
        st.rerun()
    
    answer_input = st.text_input(q, key=f"q_{st.session_state.question_index}")
    
    if st.session_state.warning:
        st.warning("⚠️ Please enter an answer before submitting.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Submit Answer"):
            if not answer_input.strip():
                st.session_state.warning = True
                st.rerun()
            else:
                st.session_state.warning = False
                st.session_state.user_answers.append((q, answer_input))
                if is_answer_correct(answer_input, correct_answer):
                    st.session_state.score += 1
                st.session_state.question_index += 1
                st.session_state.start_time = time.time()
                st.session_state.last_update = time.time()
                
                if st.session_state.question_index >= total:
                    st.session_state.completed = True
                st.rerun()
    
    with col2:
        if st.button("⏭️ Skip Question"):
            st.session_state.user_answers.append((q, "⏭️ Skipped"))
            st.session_state.question_index += 1
            st.session_state.start_time = time.time()
            st.session_state.last_update = time.time()
            
            if st.session_state.question_index >= total:
                st.session_state.completed = True
            st.rerun()

else:
    st.title("🎉 Quiz Completed!")
    total = len(st.session_state.selected_questions)
    st.markdown(f"### Subject: {st.session_state.subject}")
    st.markdown(f"**Score:** {st.session_state.score} / {total} "
                f"({(st.session_state.score / total) * 100:.0f}%)")
    
    with st.expander("🔍 Review Your Answers"):
        for i, ((q, user_ans), (_, correct_ans)) in enumerate(zip(
            st.session_state.user_answers, 
            st.session_state.selected_questions
        )):
            if user_ans.startswith("⏰") or user_ans.startswith("⏭️"):
                correct = False
                icon = f"❌ Correct: {correct_ans}"
            else:
                correct = is_answer_correct(user_ans, correct_ans)
                icon = "✅" if correct else f"❌ Correct: {correct_ans}"
            
            st.markdown(f"**Q{i+1}:** {q}")
            st.markdown(f"**Your Answer:** {user_ans}")
            st.markdown(icon)
            st.markdown("---")

    if st.button("🔁 Play Again"):
        reset_game()
        st.rerun()