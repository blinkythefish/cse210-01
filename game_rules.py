''' 

Author: Jamin Pottle
File: game_rules.py

'''

import random
import time

class GameRules():

    def __init__(self):
        self.play_game = True

        self.choice_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.main_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.player_one_game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
        self.player_two_game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
        
            # [0] is always player 1 and [1] is always player 2
        self.player_turn = [False, False]
        self.player_sign = ['x', 'o']

        self.reset_game()

    
    def reset_game(self):
        '''
        This function is in charge of resetting the game boards and picking a player to go first
        Parameters: self: used to reference class vars
        Return: none
        '''

        self.choice_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.main_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.player_one_game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
        self.player_two_game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
        
            # picks 0 or 1 randomly
        user_turn = random.randint(0,1)

            # if 0 is picked player 1 goes first, if 1 is picked player 2 goes first
        if user_turn == 0:
            self.player_turn = [True, False]

        else:
            self.player_turn = [False, True]


    def check_input(self, phrase):
        '''
        This function is in charge of checking to make sure the user 
        picked a valid input

        Parameters: user_input: is the users choice
                    choices: the list of choices the user can pick from
        Return: none

        '''

            # runs a while loop until the user enters a valid choice
        while True:

                # gets input from user
            user_input = input(phrase)

                # checks if users choice is valid
            if user_input in self.choice_board:
                if self.player_turn[0]:
                    for row in self.player_one_game_board:
                        for spot in row:
                            if spot == user_input:
                                row.remove(user_input)
                    self.choice_board.remove(user_input)

                    marker_position = self.main_board.index(user_input)
                    self.main_board[marker_position] = self.player_sign[0]
                    self.check_win(0)
                    self.player_turn = [False, True]

                else:
                    for row in self.player_two_game_board:
                        for spot in row:
                            if spot == user_input:
                                row.remove(user_input)
                    self.choice_board.remove(user_input)

                    marker_position = self.main_board.index(user_input)
                    self.main_board[marker_position] = self.player_sign[1]
                    self.check_win(1)
                    self.player_turn = [True, False]
            
                break
            else:
                if user_input.lower().strip() == 'q':
                    self.play_game = False
                    break
                print('Please enter a valid choice.')


    def check_win(self, player):
        if player == 0:
            
            for row in self.player_one_game_board:
                if len(row) == 0:
                    print('player 1 wins')
                    self.print_board()
                    time.sleep(3)
                    self.reset_game()
        
        else: 
            
            for row in self.player_two_game_board:
                if len(row) == 0:
                    print('player 2 wins')
                    self.print_board()
                    time.sleep(3)
                    self.reset_game()

    def print_board(self):
        '''
        prints the game board for users to see
        '''

        print(f'''
        _{self.main_board[0]}_|_{self.main_board[1]}_|_{self.main_board[2]}_
        _{self.main_board[3]}_|_{self.main_board[4]}_|_{self.main_board[5]}_
        _{self.main_board[6]}_|_{self.main_board[7]}_|_{self.main_board[8]}_
        ''')