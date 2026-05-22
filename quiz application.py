import random

questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store True or False in Python?",
        "options": ["A) int", "B) str", "C) bool", "D) float"],
        "answer": "C"
    },
    {
        "question": "What does len('hello') return?",
        "options": ["A) 4", "B) 6", "C) 5", "D) 3"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) lambda", "D) def"],
        "answer": "D"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A) .pt", "B) .py", "C) .pyt", "D) .python"],
        "answer": "B"
    },
    {
        "question": "Which of these is used to take user input in Python?",
        "options": ["A) scan()", "B) read()", "C) input()", "D) get()"],
        "answer": "C"
    },
    {
        "question": "What will list(range(5)) return?",
        "options": ["A) [1,2,3,4,5]", "B) [0,1,2,3,4,5]", "C) [0,1,2,3,4]", "D) [1,2,3,4]"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ["A) //", "B) /*", "C) --", "D) #"],
        "answer": "D"
    },
    {
        "question": "What is the index of the first element in a Python list?",
        "options": ["A) 1", "B) 0", "C) -1", "D) None"],
        "answer": "B"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["A) tuple", "B) list", "C) array", "D) dict"],
        "answer": "C"
    }
]

def run_quiz():
    print("=== Welcome to the Python Quiz! ===")
    name = input("Enter your name: ")
    print(f"\nHello {name}! You will be asked {len(questions)} questions.")
    print("Type A, B, C, or D to answer.\n")
    input("Press Enter to start...")

    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")
        answer = input("Your answer: ").strip().upper()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer: {q['answer']}")

    print("\n" + "=" * 40)
    print(f"Quiz Over! {name}, your score: {score}/{len(questions)}")
    if score == len(questions):
        print(" Perfect Score! Excellent!")
    elif score >= 7:
        print(" Great job!")
    elif score >= 5:
        print(" Good effort!")
    else:
        print("Keep practicing!")
    print("=" * 40)

if __name__ == "__main__":
    run_quiz()
