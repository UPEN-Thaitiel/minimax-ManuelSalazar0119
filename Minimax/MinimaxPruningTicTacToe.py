# Constants for the game setup
BOARD_SIZE = 3       # The Tic-Tac-Toe board is 3x3
REWARD = 10          # Score for winning the game

class TicTacToe:
    def __init__(self, board):
        # Initialize the board dictionary with positions 1-9 as keys
        # 'player' will be human (O), 'computer' is AI (X)
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        # Main game loop
        # 1. Print a starting message
        # 2. Computer makes the first move
        # 3. Alternate between player and computer moves
        # 4. After each move, check if the game ended (win/draw)
        # 5. If game ended, stop the loop and print result
        # Hint: Use a while True loop and exit() when game ends
        pass  # TODO: Implement this game loop

    def print_board(self):
        # Display the current board state in 3 rows and 3 columns
        # Example layout:
        #  X | O |  
        # ---+---+---
        #    | X | O
        # ---+---+---
        #  O |   | X
        # Hint: Access self.board positions 1 to 9
        pass  # TODO: Print the board nicely
        print(self.board[1]) + "|" + self.board[2] + "|" + self.board[3] + "|"
        print(self.board[4]) + "|" + self.board[5] + "|" + self.board[6] + "|"
        print(self.board[7]) + "|" + self.board[8] + "|" + self.board[9] + "|"
      

    def is_cell_free(self, position):
        # Check if the cell at 'position' (1 to 9) is empty (' ')
        # Return True if empty, False 
        if self.board == " ":
            return True
        return False

    def update_player_position(self, player, position):
        # Place player's mark ('X' or 'O') on the board at 'position'
        # First check if the cell is free using is_cell_free()
        if self.is_cell_free(position)
            self.board[position] = player
        else:
            print"error: cannot insert here"
            self.move_player()
            
    def check_game_state(self):
        # Print the current board (call print_board())
        # Check if the game is a draw (no free cells and no winner)
        # If draw, print "Draw!" and end the program
        # Check if the player or computer has won by calling is_winning()
        # If someone won, print who won and end the program
        pass  # TODO: Implement checks and use exit() when game ends
        

    def is_winning(self, player):
        # Check if 'player' ('X' or 'O') has any winning combination:
        # - 3 in any row
        # - 3 in any column
        # - 3 in either diagonal
        # Return True if winning condition met, else False
        # Hint: Use loops to check rows and columns, and manual checks for diagonals
        pass  # TODO: Implement win condition logic
        if self.board[1] == player and self.board[5] ==player and self.board[9] == player :
            return True
        if self.board[3] == player and self.board[5] ==player and self.board[7] == player :
            return True
           for i in range (1,4):
               if self.board[i] == "0":
                   temp_c +=1
               elif self.board[1] == "X"
                   temp_x +=1
            if temp_c or temp_x == 3:
                return True
                 
        n=1  1,2,3
        n=2  4,5,6
        n=3  7,8,9
        
            

    def is_draw(self):
        # Check if all cells are occupied (no spaces ' ') and no winner
        # Return True if draw, False otherwise
        # Hint: Iterate over all board positions, if any cell is ' ', return False
        pass  # TODO: Implement draw check

    def move_player(self):
        # Ask the human player to input a position (1 to 9)
        # Validate input is an integer between 1 and 9
        # Update the board with player's move by calling update_player_position()
        # If invalid input, ask again until valid
        pass  # TODO: Implement input reading and validation

    def move_computer(self):
        # Computer chooses best move using Minimax algorithm with alpha-beta pruning:
        # 1. Initialize best_score to -infinity, best_move to None
        # 2. For every free cell on board:
        #    a. Temporarily place computer's mark ('X') there
        #    b. Call minimax() with depth=0, alpha=-inf, beta=+inf, is_maximizer=False
        #    c. Undo the temporary move
        #    d. If returned score > best_score, update best_score and best_move
        # 3. After checking all moves, place computer's mark on best_move position
        # 4. Call check_game_state() to see if game ended
        pass  # TODO: Implement AI move selection

    def minimax(self, depth, alpha, beta, is_maximizer):
        # Recursive Minimax algorithm with alpha-beta pruning:
        # Base cases:
        #  - If computer has won, return REWARD - depth (prefer faster wins)
        #  - If player has won, return -REWARD + depth (prefer slower losses)
        #  - If draw, return 0
        #
        # Recursive step:
        #  - If is_maximizer (computer's turn):
        #     * Initialize best_score = -infinity
        #     * For each free cell:
        #        - Place computer's mark temporarily
        #        - Call minimax(depth+1, alpha, beta, False)
        #        - Undo move
        #        - Update best_score with max(score, best_score)
        #        - Update alpha = max(alpha, best_score)
        #        - If alpha >= beta, prune remaining branches (break)
        #     * Return best_score
        #
        #  - Else (player's turn):
        #     * Initialize best_score = +infinity
        #     * For each free cell:
        #        - Place player's mark temporarily
        #        - Call minimax(depth+1, alpha, beta, True)
        #        - Undo move
        #        - Update best_score with min(score, best_score)
        #        - Update beta = min(beta, best_score)
        #        - If alpha >= beta, prune remaining branches (break)
        #     * Return best_score
        pass  # TODO: Implement minimax with alpha-beta pruning logic


if __name__ == '__main__':
    # Create empty board dictionary with keys 1 to 9, all set to space ' '
    board = {pos: ' ' for pos in range(1, 10)}

    # Instantiate TicTacToe game with this board
    game = TicTacToe(board)

    # Start the game loop
    game.run()
