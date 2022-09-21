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

    game = game_rules.GameRules()

        # runs the game of tic tac toe till loop is broken
    while True:
        
        if not game.play_game:
            break

        game.print_board()

        player_turn = game.player_turn

        if player_turn[0]:
            game.check_input('Player 1 pick a choice 1-9 ')

        else: 
            game.check_input('Player 2 pick a choice 1-9 ')

    print('Game has ended.')
        





if __name__ == '__main__':
    main()