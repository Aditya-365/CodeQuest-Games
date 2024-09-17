from QuizData import question_data
import random

def QuizBrain() :
    score = 0
    print("Welcome to the Quiz Program.")
    print("Here, we will test you with 4 questions.")
    print("")
    for i in range(1,5) :
        random_number = random.randint(0,29)
        Question = question_data[random_number]["text"]
        Answer = question_data[random_number]["answer"]
        U_answer = input(f"{Question} \nPlease enter your answer(True/False) : ").title()
        if U_answer == Answer :
            score += 1
            print(f"Your Current Score is {score}")
        else :
            score += 0
            print(f"Your Current Score is {score}")
    print(f"Your final score is {score}")
    print("Thank You for Playing our Game.")

QuizBrain()