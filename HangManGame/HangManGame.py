import random
from HangManWordList import *

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

lives = 6

display = []
for _ in range(word_length):
    display += "_"


print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter
          
    if guess not in chosen_word :
      lives = lives - 1
      print(stages[lives])

# The line below turns the list 'display' into a string format 
# and it appears neat during the print/output
    print(f"{' '.join(display)}")

    if "_" not in display :
        end_of_game = True
        print("You win.")

    if lives == 0:
      end_of_game = True
      print("You lose")