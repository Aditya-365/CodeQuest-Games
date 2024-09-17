import random

answer = random.randint(1,100)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100. ")
print(f"btw, The answer is {answer}")


difficulty_level = input("Please choose a difficulty level, 'easy' or 'hard'  :  ").lower()
if difficulty_level == 'easy' :
    print("You have 10 attempts to guess the number.")
    no_of_guesses = 10

else :
    print("You have 5 attempts to guess the number.")
    no_of_guesses = 5


guess = int(input("Make a Guess : "))
while guess != answer :
    if guess > answer :
        print("Too high")
    else :
        print("Too low")
    no_of_guesses -= 1
    print("Guess again.")
    print(f"You have {no_of_guesses} chances to go. ")
    if no_of_guesses == 0 :
        print("You Lose.")
        break
    elif guess == answer : 
        print("You Won.")
        break
    else :
        guess = int(input("Make a Guess : "))