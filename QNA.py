import re
import random

# Q&A Pairs containing questions and answers
qa_pairs = {
    "application process": {
        "question": "Can you walk me through the steps required to apply to your university?",
        "answer": "To apply to our university, you'll need to complete an online application form, submit your high school transcripts, provide standardized test scores, write a personal statement, and obtain letters of recommendation. Deadlines and additional requirements may vary, so check the specific details for each program."
    },
    "financial aid": {
        "question": "What types of financial support are available for students? Can you explain the differences between scholarships, grants, and loans?",
        "answer": "Financial support for students includes scholarships, grants, and loans. Scholarships are typically merit-based and do not need to be repaid. Grants are usually need-based and also do not require repayment. Loans, on the other hand, must be repaid with interest after graduation. Be sure to complete the FAFSA to determine your eligibility for federal aid."
    },
    "campus life": {
        "question": "What can students expect from campus life at your university? Are there popular events or traditions that students enjoy?",
        "answer": "Campus life at our university is vibrant and diverse. Students can join a variety of clubs, participate in intramural sports, and attend numerous events such as cultural festivals, guest lectures, and social gatherings. One of our popular traditions is the annual Spring Carnival, which includes games, food, and performances."
    },
    "academic programs": {
        "question": "Could you provide an overview of the academic programs your university offers, particularly in the fields of technology and business?",
        "answer": "Our university offers a wide range of academic programs, including strong departments in technology and business. In technology, we have programs in computer science, engineering, and information systems. Our business school offers degrees in finance, marketing, management, and entrepreneurship. Each program is designed to provide both theoretical knowledge and practical skills."
    },
    "student support services": {
        "question": "What kinds of support services does your university provide to help students succeed academically and personally?",
        "answer": "We offer comprehensive support services including academic advising, career counseling, tutoring, and mental health services. Our academic advisors help students plan their coursework and stay on track for graduation. Career services assist with job searches, internships, and resume building. We also provide wellness programs and mental health resources to ensure students' well-being."
    },
    "housing options": {
        "question": "What are the housing options for students at your university? Can you describe both on-campus and off-campus choices?",
        "answer": "Students at our university can choose from a variety of housing options. On-campus options include traditional dormitories, suite-style living, and themed housing communities. Off-campus housing includes apartments and houses within close proximity to the campus. On-campus housing provides convenience and a sense of community, while off-campus housing offers more independence."
    },
    "internship opportunities": {
        "question": "Does your university offer opportunities for internships? How can students gain work experience while studying?",
        "answer": "Yes, we have a robust internship program that helps students gain practical work experience. Students can find internships through our career services office, which partners with various companies and organizations. Internships can be completed during the summer or part-time during the academic year, allowing students to apply classroom knowledge in real-world settings."
    },
    "study abroad programs": {
        "question": "Are there study abroad programs available at your university? What are some of the destinations students can choose from?",
        "answer": "Yes, our university offers a variety of study abroad programs. Students can choose from destinations in Europe, Asia, Latin America, and more. These programs range from a few weeks to a full academic year. Studying abroad provides a unique opportunity to immerse yourself in a new culture, learn a new language, and gain a global perspective on your field of study."
    },
}

# Fun facts about college life
fun_facts = [
    "Did you know? The first university in the United States, Harvard, was established in 1636.",
    "Fun fact: On average, college students change their major three times during their studies!",
    "Here's an interesting fact: College students spend roughly 30% of their time sleeping.",
    "Did you know? The longest lecture ever recorded lasted 138 hours, delivered by Dr. Richard F. Taflinger at East Carolina University in 2007.",
    "Fun fact: The term 'quiz' was coined in the late 18th century by a Dublin theater owner who bet he could introduce a new word into the English language within 24 hours.",
]

# Farewell messages
farewell_messages = [
    "Thanks for chatting with me! If you have more questions in the future, don't hesitate to return.",
    "It was great talking to you! Have an excellent day!",
    "Goodbye for now! Remember, I'm here to help whenever you need assistance.",
    "Until next time! Take care and best of luck on your college journey.",
]

# Empty lists to store conversation history and user information
conversation_log = []


def welcome_message():
    """Display welcome message."""
    print("Hello! Welcome to the College Q&A Bot. I'm here to help you with information about college life, admissions, and more.")
    print("To start, Please Introduce Yourself?")
    user_name = input("Your name: ")
    print(f"Nice to meet you, {user_name}! Feel free to ask me any questions you have about college.")


def handle_question(question):
    """Respond to the user's question with an appropriate answer."""
    if "fun fact" in question.lower():
        return random.choice(fun_facts)
    
    for keyword, qa_pair in qa_pairs.items():
        if re.search(keyword, question, re.IGNORECASE):
            return qa_pair["answer"]

    return "I'm not sure I understand that question. Could you rephrase it or ask something else?"


def chat_bot():
    """Main function to run the Q&A bot."""
    welcome_message()
    while True:
        question = input("You: ")
        answer = handle_question(question)
        print("Bot:", answer)
        conversation_log.append((question, answer))

        # Check if the user wants to end the conversation
        if question.lower() in ["goodbye", "bye", "quit"]:
            print(random.choice(farewell_messages))
            break


if __name__ == "__main__":
    chat_bot()
