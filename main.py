from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question['answer']))

zoha_quiz = QuizBrain(question_bank)

while zoha_quiz.remaining_questions():
    zoha_quiz.next_question()

print("You finished the test")
print(f"Your final score was {zoha_quiz.points}/{len(question_bank)}")