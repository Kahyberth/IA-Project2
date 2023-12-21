from Logic.rules import Rules
from Logic.minimax import minimax, filter_valid_moves


class Game:
    def __init__(self, board):

        self.board = board
        self.rules = Rules(self.board)

    def update(self, x1, y1, x2, y2, number_of_movements=1):
        status, count, board = self.rules.move(x1, y1, x2, y2, number_of_movements)
        print('count: ', status)
        if not status:
            print("Invalid movement")
            count = number_of_movements
            self.print_board()
            return count, board
        self.print_board()
        return count, board


    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def print_board2(self, board):
        for i in range(len(board)):
            print(board[i])

    def checkmv(self, x2, y2):
        number = self.rules.number_of_movements(x2, y2)
        print(number)

    def check_field(self, y2):
        print(self.rules.check_column(y2))

    def check_winner(self):
        print(self.rules.check_winner())

    def check_distance(self, y1, x2, y2, number_of_movements):
        print(self.rules.check_distance(y1, x2, y2, number_of_movements))

    def check_game_over(self):
        print(self.rules.check_game_over())

    def minimax(self, board, mark):
        return minimax(board, mark)

    def filter_valid_moves(self, validation_range):
        board = self.board
        return filter_valid_moves(board, validation_range)


