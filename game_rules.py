''' 

Author: Jamin Pottle
File: game_rules.py

'''

import random
import time

class GameRules():

    def __init__(self):
        '''
        sets default vars that will be used through out the class
        Parameters: none
        Return: none
        '''
            # checks if game is still going
        self.play_game = True

            # checks if user is picking a choice that has not been picked
        self.choice_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            # numbers are replaced with users marker as they select a proper value
        self.main_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            # all the possible ways for each player to win
        self.player_one_game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
        self.player_two_game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
        
            # [0] is always player 1 and [1] is always player 2
        self.player_turn = [False, False]
        self.player_sign = ['x', 'o']

            # does a reset on the game to set a players turn
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

        Parameters: phrase: is a statement or question passed in for the user
                            to enter a response to, it will be checked against
                            a set of values to make sure the user gives a proper
                            response
        Return: none

        '''

            # runs a while loop until the user enters a valid choice
        while True:

                # gets input from user
            user_input = input(phrase)

                # checks if users choice is valid
            if user_input in self.choice_board:
                
                    # checks what user is going [0] is Player 1
                    # otherwise it is player 2 going
                if self.player_turn[0]:

                        # goes through and checks each array to   
                        # remove the players choice to keep track 
                        # of players moves
                    for row in self.player_one_game_board:

                            # checks individual value in each sub array
                        for spot in row:    

                                # checks if the user's input matches the
                                # a choice in the users array, and if it
                                # matches then it is removed from the player's
                                # array and then removed from the choice board
                            if spot == user_input:
                                row.remove(user_input)
                    self.choice_board.remove(user_input)

                        # the players marker is then added to the main_board
                        # which is then printed later
                    marker_position = self.main_board.index(user_input)
                    self.main_board[marker_position] = f'\033[91m{self.player_sign[0]}\033[0m'

                        # does a check if the player wins
                    self.check_win(0)

                        # changes it so it is the other players turn
                    self.player_turn = [False, True]

                else:
                    for row in self.player_two_game_board:
                        for spot in row:
                            if spot == user_input:
                                row.remove(user_input)
                    self.choice_board.remove(user_input)

                    marker_position = self.main_board.index(user_input)
                    self.main_board[marker_position] = f'\033[94m{self.player_sign[1]}\033[0m'
                    self.check_win(1)
                    self.player_turn = [True, False]
            
                break

                # this portion is for if the user does not enter
                # a valid input
            else:   
                    # if the user enters q then the game will be 
                    # quit and will no longer be played
                if user_input.lower().strip() == 'q':
                    self.play_game = False
                    break

                    # lets the user know they did not enter a valid input
                print('\n\n\n\033[93mPlease enter a valid choice.\033[0m')

                    # prints the board for the users to see
                self.print_board()


    def check_win(self, player):
        '''
        this function is run after each users turn to check if they made a winning move
        Parameters: player: is the player number 0 for player 1 and 1 for player 2
        return: none
        '''

            # checks if player one is the one that went 
        if player == 0:
            
                # runs through each array in the players game board
            for row in self.player_one_game_board:

                    # if the length of an array is 0 then that means 
                    # the player has won, and will reset the game
                if len(row) == 0:
                    print('\n\n\n\033[91mPlayer 1 Wins!!\033[0m')
                    self.print_board()
                    time.sleep(3)
                    self.reset_game()
        
        else: 
            
            for row in self.player_two_game_board:
                if len(row) == 0:
                    print('\n\n\n\033[94mPlayer 2 Wins!!\033[0m')
                    self.print_board()
                    time.sleep(3)
                    self.reset_game()


            # checks if the choice board is out of options
            # if it is, then a message is displayed showing
            # a cats game then the game is reset
        if len(self.choice_board) == 0:
            print('\n\n\n\033[93mCats game!\033[0m')
            self.reset_game()


    def print_board(self):
        '''
        prints the game board for users to see
        parameters: none
        return: none
        '''

            # uses the main_board array to display what moves 
            # the players have made
        print(f'''\n\n\n
        _{self.main_board[0]}_|_{self.main_board[1]}_|_{self.main_board[2]}_
        _{self.main_board[3]}_|_{self.main_board[4]}_|_{self.main_board[5]}_
        _{self.main_board[6]}_|_{self.main_board[7]}_|_{self.main_board[8]}_
        ''')