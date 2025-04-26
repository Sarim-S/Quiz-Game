class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.points = 0

    def remaining_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {question.text} (True / False): ")
        self.check_answer(choice, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.points += 1
            print(f"You were correct! \nThe correct answer was: {correct_answer}")
        else:
            print("Incorrect :( ")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.points}/{self.question_number} \n")


