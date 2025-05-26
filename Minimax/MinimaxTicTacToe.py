BOARD_SIZE = 3
REWARD = 10

class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        print("Welcome to Tic-Tac-Toe 2")
        
        while True:
            self.move_computer()
            self.move_player()

    def print_board(self):
        print("\nCurrent Board:")
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print("---+---+---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print("---+---+---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} \n")

    def is_cell_free(self, position):
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
            return True
        print("Error: Position already taken!")
        return False

    def is_winning(self, player):
       
        for i in range(1, 8, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        for i in range(1, 4):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
       
        if self.board[1] == self.board[5] == self.board[9] == player:
            return True
        if self.board[3] == self.board[5] == self.board[7] == player:
            return True
        return False

    def is_draw(self):
        
        for pos in range(1, 10):
            if self.is_cell_free(pos):
                return False
        return True

    def check_game_state(self):
        
        self.print_board()
        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()
        elif self.is_winning(self.player):
            print("You win!")
            exit()
        elif self.is_draw():
            print("Draw!")
            exit()

    def move_player(self):
        
        while True:
            try:
                position = int(input("Enter your move (1-9): "))
                if 1 <= position <= 9:
                    if self.update_player_position(self.player, position):
                        break
                    else:
                        continue
                print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Please enter a valid number!")

    def move_computer(self):
        
        best_score = -float('inf')
        best_move = None
        
        for pos in range(1, 10):
            if self.is_cell_free(pos):
                self.board[pos] = self.computer
                score = self.minimax(0, False)
                self.board[pos] = ' '
                
                if score > best_score:
                    best_score = score
                    best_move = pos
        
        self.board[best_move] = self.computer
        print(f"Computer plays at position {best_move}")
        self.check_game_state()

    def minimax(self, depth, is_maximizer):
        
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0
            
        if is_maximizer:
            best_score = -float('inf')
            for pos in range(1, 10):
                if self.is_cell_free(pos):
                    self.board[pos] = self.computer
                    score = self.minimax(depth + 1, False)
                    self.board[pos] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for pos in range(1, 10):
                if self.is_cell_free(pos):
                    self.board[pos] = self.player
                    score = self.minimax(depth + 1, True)
                    self.board[pos] = ' '
                    best_score = min(score, best_score)
            return best_score


if __name__ == '__main__':
    
    board = {pos: ' ' for pos in range(1, 10)}

    game = TicTacToe(board)

    game.run()
