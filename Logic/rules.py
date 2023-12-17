# Rules
class Rules:
    def __init__(self, board):
        self.board = board

    # Count the number of squares
    def number_of_movements(self, x2, y2):
        # x2 = row
        # y2 = column
        count = 0
        for i in range(len(self.board)):
            if (self.board[i][y2] == '🟥' or self.board[i][y2] == '🟦') and self.board[i][y2] != '⬜' and i != x2:
                print(self.board[i][y2])
                count += 1
        return count

    def move(self, x1, y1, x2, y2, number_of_movements=1):
        board = self.board
        count = 0
        if not self.check_movement(y2):
            return False, board, count

        if not self.check_distance(y1, x2, y2, number_of_movements):
            return False, board, count

        board[x2][y2] = board[x1][y1]
        board[x1][y1] = '⬜'

        count = self.number_of_movements(x2, y2)
        return True, board, count

    def check_winner(self):
        board = self.board
        points = 0
        red_square = []
        blue_square = []

        for i in range(len(board)):
            red_square.append(board[i][0:7])
            blue_square.append(board[i][8:])

        points = {
            # Red
            '0': points + 5,
            '2': points + 3,
            '4': points + 2,
            '6': points + 1,
            # Blue
            '8': points + 1,
            '10': points + 2,
            '12': points + 3,
            '14': points + 5,
        }

        red_points = 0
        blue_points = 0

        # i = row
        # j = column

        for i in range(len(red_square)):
            for j in range(len(red_square[i])):
                if red_square[i][j] == '🟥' and j % 2 == 0:
                    if not self.check_field(j):
                        red_points += points[str(j)]
                    red_points += points[str(j)]
                if blue_square[i][j] == '🟦' and j % 2 == 0:
                    if not self.check_field(j):
                        blue_points += points[str(j)]

        return red_points, blue_points

    def check_loser(self):
        red_points, blue_points = self.check_winner()
        if red_points > blue_points:
            print("Blue is the loser")
        else:
            print("Red is the loser")

    def check_draw(self):
        red_points, blue_points = self.check_winner()
        if red_points == blue_points:
            print("Draw")

    def check_game_over(self):
        board = self.board
        red_square = []
        blue_square = []
        for i in range(len(board)):
            red_square.append(board[i][0:7])
            blue_square.append(board[i][8:])

    def check_distance(self, y1, x2, y2, number_of_movements):
        board = self.board
        distance_board = []
        for i in range(len(board[x2][y1:y2+1])):
            print(i)
            if board[x2][y1:y2+1][i] != '⬛' and i != y1:
                distance_board.append(board[x2][y1:y2+1][i])
        if len(distance_board) > number_of_movements and board[x2][y2] != '⬛':
            return False  # You can't move there
        else:
            return True

    def check_movement(self, y2):
        board = self.board
        count = 0
        for i in range(5):
            if (board[i][y2] == '🟥' or board[i][y2] == '🟦') and board[i][y2] != '⬜':
                count += 1
        if count != 6:
            return True
        else:
            return False

    def check_field(self, y2):
        board = self.board
        count = 0
        for i in range(len(board)):
            if board[i][y2] != '🟥' or board[i][y2] != '🟦' and board[i][y2] == '⬜':
                count += 1
        if count != 6:
            return False
        else:
            return True
