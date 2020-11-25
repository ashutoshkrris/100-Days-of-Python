from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

limit = int(input("How many questions do you wish for? : "))

while quiz.still_has_questions(limit):
    quiz.next_question()

print(f"You've completed the quiz with a final score of {quiz.score} out of {quiz.question_number}.")
