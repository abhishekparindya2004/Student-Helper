import random
from storage import load_data, save_data

QUIZ_HISTORY = "quiz_history.json"

QUESTIONS = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type stores True or False values?",
        "options": ["int", "str", "bool", "list"],
        "answer": "bool"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Tech Machine Language", "Home Tool Markup Language", "Hyperlink Text Making Language"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which study technique uses repeated review over time?",
        "options": ["Cramming", "Spaced repetition", "Skipping", "Guessing"],
        "answer": "Spaced repetition"
    },
    {
        "question": "Which structure stores multiple items in Python?",
        "options": ["list", "integer", "boolean", "float"],
        "answer": "list"
    },
    {
        "question": "What is the best first step before starting an assignment?",
        "options": ["Submit quickly", "Understand requirements", "Ignore rubric", "Copy content"],
        "answer": "Understand requirements"
    },
    {
        "question": "Which operator checks equality in Python?",
        "options": ["=", "==", "!=", ">="],
        "answer": "=="
    },
    {
        "question": "What should students do to avoid plagiarism?",
        "options": ["Copy directly", "Use citations", "Hide sources", "Use no references"],
        "answer": "Use citations"
    },
    {
        "question": "Which tool is commonly used for version control?",
        "options": ["Git", "Paint", "Calculator", "Notepad only"],
        "answer": "Git"
    }
]

def start_quiz():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    score = 0

    print("\n--- Student Quiz ---")
    for index, item in enumerate(questions, start=1):
        print(f"\nQ{index}. {item['question']}")
        for option_index, option in enumerate(item["options"], start=1):
            print(f"{option_index}. {option}")

        try:
            answer_index = int(input("Your answer number: ")) - 1
            selected = item["options"][answer_index]
            if selected == item["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Correct answer: {item['answer']}")
        except (ValueError, IndexError):
            print(f"Invalid answer. Correct answer: {item['answer']}")

    percentage = (score / len(questions)) * 100
    print(f"\nYour score: {score}/{len(questions)} ({percentage:.2f}%)")

    history = load_data(QUIZ_HISTORY, [])
    history.append({"score": score, "total": len(questions), "percentage": round(percentage, 2)})
    save_data(QUIZ_HISTORY, history)

def view_quiz_history():
    history = load_data(QUIZ_HISTORY, [])
    if not history:
        print("No quiz history found.")
        return

    print("\n--- Quiz History ---")
    for index, result in enumerate(history, start=1):
        print(f'{index}. {result["score"]}/{result["total"]} - {result["percentage"]}%')

def quiz_menu():
    while True:
        print("\n--- Quiz Practice ---")
        print("1. Start Quiz")
        print("2. View Quiz History")
        print("3. Back")
        choice = input("Choose: ")

        if choice == "1":
            start_quiz()
        elif choice == "2":
            view_quiz_history()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
