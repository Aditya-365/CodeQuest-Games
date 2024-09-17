from HigherGameData import data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# def Game() :
ans = 'y'
while ans == 'y' :
    print(logo)
    print("Welcome to the Higher Lower Game.")
    score = 0
    print(f"Your Score is {score}")

    account_a = random.choice(data)
    account_b = random.choice(data)

    print(f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}")
    print(vs)
    print(f"Compare B: {account_b['name']}, {account_b['description']}, {account_b['country']}")

    guess = input("Who do you think will have more followers(A/B) : ").upper()

    if account_a['follower_count'] > account_b['follower_count'] :
        answer = 'A'
    elif account_a['follower_count'] == account_b['follower_count'] :
        answer = 'A' or 'B'
    else :
        answer = 'B'
    
    bee = 'y'
    while bee == 'y':
        if answer == guess :
            score += 1
            print(f"Your Current Score is {score}")
            account_a = account_b 
            account_b = random.choice(data)
            print(f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}")
            print(vs)
            print(f"Compare B: {account_b['name']}, {account_b['description']}, {account_b['country']}")
            guess = input("Who do you think will have more followers(A/B) : ").upper()
            if account_a['follower_count'] > account_b['follower_count'] :
                answer = 'A'
            elif account_a['follower_count'] == account_b['follower_count'] :
                answer = 'A' or 'B'
            else :
                answer = 'B'
        else :
            print("You Lose.")
            print(f"Your final score is {score}")
            bee = 'n' 
    ans = input("Do you want to play again? (y/n) : ").lower()