"""
    Hangman
      Jimmy McCue
      The program has the player to roll two dice in which some combinations print out comments
      06-05-2025
"""
import random

die_one = 1
die_two = 1
game_on = True
user_input = ''

while game_on:

  user_input = input('Press enter to roll the dice\n Type q and hit enter to quit ')

  if user_input == 'q':
    game_on = False

  else:
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)

    print(f'{die_one},{die_two} = {die_one + die_two}')

    if die_one == die_two:
      if die_one == 1:
        print('"Snake Eyes"')
      elif die_one == 2:
        print('"Little Joe from Kokomo"')
      elif die_one == 3:
        print('"Jimmy Hicks from the Sticks"')
      elif die_one == 4:
        print('"Eighter from Decatur"')
      elif die_one == 5:
        print('"Puppy Paws"')
      elif die_one == 6:
        print('"Boxcars"')
    elif die_one + die_two == 3:
      print('"Ace Caught a Duece"')
    elif die_one + die_two == 5:
      print('"Little Phoebe"')
    elif die_one + die_two == 9:
      print('"Nina from Pasadena"')
    elif die_one + die_two == 7:
      if die_one == 6 or die_two ==6:
        print('"Six Ace"')
    elif die_one + die_two == 11:
      if die_one == 6 or die_two ==6:
        print('"Six Five no Jive"')