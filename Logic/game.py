from Logic.rules import Rules


class Game:
    def __init__(self, board):

        self.board = board
        self.rules = Rules(self.board)

    def update(self, x1, y1, x2, y2, number_of_movements=1):
        self.board, count = self.rules.move(x1, y1, x2, y2, number_of_movements)
        print(count)
        for i in range(len(self.board)):
            print(self.board[i])
        return count

    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def checkmv(self, x2, y2):
        number = self.rules.number_of_movements(x2, y2)
        print(number)

    def check_field(self, y2):
        print(self.rules.check_field(y2))


    def check_winner(self):
        print(self.rules.check_winner())

    def check_distance(self, x2, y2, number_of_movements):
        print(self.rules.check_distance(x2, y2, number_of_movements))


