from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question['answer']))

quiz = QuizBrain(question_bank)

while quiz.remaining_questions():
    quiz.next_question()

print("You finished the test")
print(f"Your final score was {quiz.points}/{len(question_bank)}")