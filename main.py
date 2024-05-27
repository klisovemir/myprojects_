from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []
for question in question_data:
    q1 = question['text']
    a1 = question['answer']
    new_question = Question(q1, a1)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")









