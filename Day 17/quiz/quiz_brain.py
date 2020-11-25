class QuizBrain:
    """QuizBrain class"""

    def __init__(self, question_list):
        """Constructor"""
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q{self.question_number}. {current_question.text} (True/False) : ")
        self.check_answer(current_question.answer, user_answer)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("Yay! You got it right.")
        else:
            print("Oops! You missed it.")
            print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}.")

    def still_has_questions(self, limit):
        return self.question_number < limit
