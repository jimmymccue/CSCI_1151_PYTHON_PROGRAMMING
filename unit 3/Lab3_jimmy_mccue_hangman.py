"""
    Hangman
      Jimmy McCue
      The program ask users to guess a secret random number between 1 and 15 and the game 
        plays out like a traditional hangman style game.
      06-03-2025

"""

import random

hang_man = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
random_number = random.randint(1,15)
wrong_guesses = 0
player_guess = 0
game_over = 'no'

print(f'If you are ready to play "Hangman" pick a number between 1 and 15\nIf the guess is out of the bounds of 1-15 it will be counted as a wrong guess')

while wrong_guesses < 6:

  player_guess = int(input('Enter your guess and then hit the enter button:  '))

  if player_guess == random_number:
    game_over = 'yes'
    print("Congratulations, you've guessed the number")
    break
  else:
    wrong_guesses += 1
    print(f'draws {hang_man[wrong_guesses -1]}')

  if wrong_guesses == len(hang_man):
    game_over = 'yes'
    print('You Lose!')
    break

  print(f'Is game over- {game_over}')
  
print(f'Is game over- {game_over}')
