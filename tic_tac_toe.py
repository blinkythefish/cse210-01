''' 

Author: Jamin Pottle
File: tic_tac_toe.py

'''


import game_rules


def main():
    '''
    This function is the main function of the tic tac toe program
    Parameters: none
    Return: none
    '''

        # creates an instance of GameRules 
    game = game_rules.GameRules()

        # runs the game of tic tac toe till loop is broken
    while True:
        
            # checks if the game is still being played
        if not game.play_game:
            break

        game.print_board()

            # checks what player is going
        player_turn = game.player_turn

            # if its player 1's turn it will ask them for input
            # otherwise it will ask player 2
        if player_turn[0]:
            game.check_input('\033[91mPlayer 1\033[0m pick a choice 1-9 ')

        else: 
            game.check_input('\033[94mPlayer 2\033[0m pick a choice 1-9 ')

        # gives a message the game was quit
    print('\n\n\n\033[93mGame has ended.\033[0m\n\n\n')
        




    # runs main function if tic_tac_toe.py is the file that is run
if __name__ == '__main__':
    main()