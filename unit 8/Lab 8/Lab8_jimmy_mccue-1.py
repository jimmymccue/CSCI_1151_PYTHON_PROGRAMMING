"""
      Jimmy McCue
      The program allows two players to compete against each other by flipping a coin and depending 
      on the outcome winning the other players coin.  Player One wins when coins match.  Player two 
      wins when the coins are opposite.
      06-16-2025
"""

from coin import Coin

def main():
    
    play_continues = 'y'
    player_one_coin = Coin()
    player_two_coin = Coin()
    rounds_played = 0

    while play_continues.lower() == "y" and player_one_coin.get_amount() > 0 and player_two_coin.get_amount() > 0:

        
        play_continues = input('\nWould Player One like to toss their coin enter Y: ')

        if play_continues.lower() == 'y':
          
            play_continues = input('\nWould Player Two like to toss their coin enter Y: ')

            if play_continues.lower() == 'y':

                player_one_coin.toss()
                print(f'\nPlayer One flipped {player_one_coin.get_sideup()}')

                player_two_coin.toss()
                print(f'Player Two flipped {player_two_coin.get_sideup()}')

                if player_one_coin.get_sideup() == player_two_coin.get_sideup():
                    player_one_coin.set_amount(1)
                    player_two_coin.set_amount(-1)
                    print('Player One wins!')
                else:
                    player_one_coin.set_amount(-1)
                    player_two_coin.set_amount(1)
                    print('Player Two wins!')
                    
                print(f'Player One has {player_one_coin.get_amount()} coins')
                print(f'Player Two has {player_two_coin.get_amount()} coins')
                rounds_played += 1
                    
    print(f'\nGame Ends after {rounds_played} rounds played')
    print(f'Player One has {player_one_coin.get_amount()} coins')
    print(f'Player Two has {player_two_coin.get_amount()} coins')

    if player_one_coin.get_amount() > player_two_coin.get_amount():
        print('Player One wins the game!')
    elif player_one_coin.get_amount() < player_two_coin.get_amount():
        print('Player Two wins the game!')
    else:
        print('The Players Tied!')

if __name__ == "__main__":
    main()
