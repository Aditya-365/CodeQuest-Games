import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to the Game of Rock-Paper-Scissors. ")
user_choice = int(input("Please enter your choice : 0 for Rock , 1 for paper , and 2 for scissors. "))

computer_choice = random.randint(0,2)

if user_choice == 0 :
  print("Your choice : \n " + rock)
  if computer_choice == 1 :
    print("Computer choice : \n " + paper + "\n")
    print("Computer wins ")
  elif computer_choice == 2 :
    print("Computer choice : \n " + scissors + "\n")
    print("You win")
  else :
    print("Computer choice : \n " + rock + "\n")
    print("It's a draw ")

  

elif user_choice == 1 :
  print("Your choice : \n " + paper)
  if computer_choice == 1 :
    print("Computer choice : \n " + paper + "\n")
    print("It's a draw ")
  elif computer_choice == 2 :
    print("Computer choice : \n " + scissors + "\n")
    print("Computer wins ")
  else :
    print("Computer choice : \n " + rock + "\n")
    print("You win ")
    
else :
  print("Your choice : \n " + scissors)
  if computer_choice == 1 :
    print("Computer choice : \n " + paper + "\n")
    print("You win ")
  elif computer_choice == 2 :
    print("Computer choice : \n " + scissors + "\n")
    print("It's a draw ")
  else :
    print("Computer choice : \n " + rock + "\n")
    print("Computer wins ")
