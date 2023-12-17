from Logic.game import Game
board = [
            ['🟥', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦', '⬛', '🟦1'],
            ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦2'],
            ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦3'],
            ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦4'],
            ['🟥', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '🟦5'],
            ['🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟥', '⬛', '🟦6'],
        ]

game = Game(board)

input("Press Enter to continue...")

number_of_movements = 1
while True:
    print("---Linja---")
    print('Number of movements: ', number_of_movements)
    x1 = int(input("Ingrese el valor de x1: "))
    y1 = int(input("Ingrese el valor de y1: "))
    x2 = int(input("Ingrese el valor de x2: "))
    y2 = int(input("Ingrese el valor de y2: "))
    input("Press Enter to continue...")
    number_of_movements = game.update(x1, y1, x2, y2, number_of_movements)













