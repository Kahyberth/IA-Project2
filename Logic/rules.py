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
        point = 0
        red_square = []
        blue_square = []

        for i in range(len(board)):
            blue_square.append(board[i][0:7])
            red_square.append(board[i][8:])


        points = {
            '0': point + 5,
            '2': point + 3,
            '4': point + 2,
            '6': point + 1,
        }

        red_points = 0
        blue_points = 0

        # i = row
        # j = column

        column = 0
        for row in range(len(red_square) + 1):
            counter = 0
            for j in range(len(red_square)):
                if column % 2 == 0:
                    if red_square[j][column] == '🟥':
                        red_points += points[str(column)]
                    if blue_square[j][column] == '🟦':
                        blue_points += points[str(column)]
            column += 1

        if red_points > blue_points:
            print('Points of the red: ', red_points)
            print('Points of the blue: ', blue_points)
            print("Blue is the loser")
        elif red_points == blue_points:
            print('Points of the red: ', red_points)
            print('Points of the blue: ', blue_points)
            print("Draw")
        else:
            print('Points of the red: ', red_points)
            print('Points of the blue: ', blue_points)
            print("Red is the loser")

        return red_points, blue_points


    def check_draw(self):
        red_points, blue_points = self.check_winner()
        if red_points == blue_points:
            print("Draw")

    def check_game_over(self):
        board = self.board
        red_square = []
        blue_square = []
        for i in range(len(board)):
            blue_square.append(board[i][0:7])
            red_square.append(board[i][8:])
        counter = 0
        for i in range(len(blue_square)):
            for j in range(len(blue_square)):
                if blue_square[i][j] == '🟥':
                    counter += 1

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
