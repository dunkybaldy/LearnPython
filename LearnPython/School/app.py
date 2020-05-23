from Question import Question
from Student import Student

student1 = Student("Dunc", "Computing", 3.6, False)
print(student1.on_honor_roll())

questions = [
    Question("How old am I?\n(a)15\n(b)24\n(c)25\n", "b"),
    Question("What is my name?\n(a)Dunkybaldy\n(b)Duncan\n(c)BoinerBean\n", "c")
]

def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print(f"\nYou got {score} out of {len(questions)}")

run_test(questions)