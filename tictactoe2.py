""" 
File: tictactoe.py try again
Author: Mark Richmodn
This program implements a Tic Tac Toe game.
"""

#from types import ClassMethodDescriptorType


class Board():
    """
    Board class - All information and activities of the playing board
    """
    def __init__(self, selected_size):
        # Set initial Variables
        
        # number of spaces per side
        self.edge_size = selected_size
        # Number of spaces in the whole puzzle
        self.size = selected_size * selected_size
        # Define text string the is used to print the board.
        self.board = ""
        # Define board
        self.board_space = []
        # Populate board
        for i in range (self.size):
            self.board_space.append(i+1)   
        
    def draw_board(self):
        # Draw current board object

        print("")
        self.board = ""

        for i in range(self.size):
            # Print board one space at a time
            if self.edge_size > 3 and (i < 9 or self.board_space[i] != i+1):
                self.board += " "
            self.board += "{}".format(self.board_space[i])
            if (i % self.edge_size != self.edge_size -1):
                self.board += "|"
            else:
                # Print line between rows
                self.board += "\n"
                if i != self.size - 1:
                    if self.edge_size > 3 and (i < 9 or self.board_space[i] != i+1 or (i > 8)):
                        self.board += "-"
                    self.board += "-" 
                    for i in range(self.edge_size-1):
                        self.board += "+-" 
                        if self.edge_size > 3 and (i < 9 or self.board_space[i] != i+1):
                            self.board += "-"
                    self.board += "\n" 
        print(self.board)
        
    def mark_board(self, current_player_marker, selected_position):
        # Mark the board with the player's choice
        if self.board_space[selected_position-1] == "x" or self.board_space[selected_position-1] == "o":
            print("This space is already chosen.  Please select another.")
            return (False)
        self.board_space[selected_position-1]=current_player_marker
        return (True)

    def check_rows(self):
        # Check each row to see if it is filled with matching marks
        row_filled = True
        cell_value = "x"
        for i in range (self.edge_size):
            # For each row
            for j in range (self.edge_size):
                # For each space in the row
                if j == 0:
                    cell_value = self.board_space[(i*self.edge_size)+j]
                row_filled = row_filled and (self.board_space[(i*self.edge_size)+j] == cell_value)
            if row_filled:
                return(row_filled)
            if i != self.edge_size - 1:
                row_filled = True
        return(row_filled)
            
    def check_columns(self):
        # Check each column to see if it is filled with matching marks
        column_filled = True
        cell_value = "x"
        for i in range (self.edge_size):
            # For each Column 
            for j in range (self.edge_size):
                # For each space in the column
                if j == 0:
                    cell_value = self.board_space[(j*self.edge_size)+i]
                column_filled = column_filled and (self.board_space[(j*self.edge_size)+i] == cell_value)
            if column_filled:
                return(column_filled)
            if i != self.edge_size - 1:
                column_filled = True
        return(column_filled)
            
    def check_diagonals(self):
        # Check each diagonal to see if it is filled with matching marks

        # For top left to bottom right diagonal
        diagonal_filled = True
        for j in range (0, self.size, self.edge_size + 1):
            # For each space in the diagonal
            if j == 0:
                cell_value = self.board_space[j]
            diagonal_filled = diagonal_filled and (self.board_space[j] == cell_value)
        if diagonal_filled:
            return(diagonal_filled)

        # For bottom left to top right diagonal
        diagonal_filled = True
        for j in range (self.size-self.edge_size, self.edge_size-2, -1*(self.edge_size-1)):
            # For each space in the diagonal
            if j == self.size-self.edge_size:
                cell_value = self.board_space[j]
            diagonal_filled = diagonal_filled and (self.board_space[j] == cell_value)

        return(diagonal_filled)

    def check_draw(self):
        # Check to see if all spaces are filled and therefore it is a draw
        for i in range(self.size):
            # If any spaces still contain numbers, it is not a draw
            if self.board_space[i] == i+1:
                return(False)
        return(True)       

    def is_game_over(self):
        # Check to see if the game is over
        # Check for possible winners
        if self.check_rows() or self.check_columns() or self.check_diagonals():
            print("Good game. Thanks for playing!\n")
            return(True)
        # Check for draw
        if (self.check_draw()):
            print("Draw. Thanks for playing!\n")
            return(True)
        return (False)


class Player():
    """
    Player class - All information and activities about a player
    """
    def __init__(self, play_marker, prompt_string):
        # Set player marker
        self.marker = play_marker
        self.prompt_string = prompt_string

    def get_marker(self):
        # Expose player marker
        return(self.marker)
               
    def get_prompt(self):
        # Expose player prompt
        return(self.prompt_string)
               
def main():
#   main function calls other functions
    board_size = int(input("Input how many spaces per side (3-9, but typically this is 3): "))

    player_x = Player("x", "x\'s turn to choose a square (1-{}): ".format(board_size**2))
    player_o = Player("o", "o\'s turn to choose a square (1-{}): ".format(board_size**2))
    
    players = []
    players.append(player_x)
    players.append(player_o)
    
    game_board = Board(board_size)
    
    game_board.draw_board()

    game_over = False

    while (not(game_over)):
        # Player x turn
        for player in range(2):
            valid_response = False
            while (not(valid_response)):
                choice = int(input(players[player].get_prompt()))
                valid_response = game_board.mark_board(players[player].get_marker(),choice)
            game_board.draw_board()
            game_over = game_board.is_game_over()
            if game_over:
                break     

if __name__ == "__main__":
    main()