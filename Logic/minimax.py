import math
import random


def filter_valid_moves(board, validation_range):
    new_valid_moves = []
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '⬛' and board[i][j] != '🟥' and board[i][
                j] != '🟦' and j <= validation_range + 2 and j != 0:
                new_valid_moves.append([i, len(board[0]) - 1 - j])
                count += 1
    return new_valid_moves


aiBlue = '🟦'
humanRed = '🟥'


def check_best_move(board, valid_moves, index):
    count = 0
    coords = filter_valid_moves(board, valid_moves)
    for i in range(len(board)):
        if (board[i][coords[index][1]] == '🟥' or board[i][coords[index][1]] == '🟦') and board[i][
            coords[index][1]] != '⬜':
            count += 1
    return count


def column(value):
    return random.randint(0, value)


def minimax(board, validation_range, mark, count=0):
    valid_coords = filter_valid_moves(board, validation_range)

    score = 0
    if count < len(valid_coords):
        score = check_best_move(board, validation_range, count)

    if count != 0:
        return score

    current_test_play_info = {'index': 0, 'score': score, 'coords': valid_coords[0]}

    all_test_play_infos = [current_test_play_info.copy()]

    for i in range(1, len(valid_coords)):
        if mark == aiBlue:
            count += 1
            result = minimax(board, validation_range, aiBlue, count)
            current_test_play_info['index'] = count
            current_test_play_info['score'] = result
            current_test_play_info['coords'] = valid_coords[i]
        else:
            result = minimax(board, validation_range, humanRed, count)
            current_test_play_info['index'] = count
            current_test_play_info['score'] = result
            current_test_play_info['coords'] = valid_coords[i]

        all_test_play_infos.append(current_test_play_info.copy())

    best_test_play = None

    if mark == aiBlue:
        best_score = -math.inf
        for i in range(len(all_test_play_infos)):
            if all_test_play_infos[i]['score'] > best_score:
                best_score = all_test_play_infos[i]['score']
                best_test_play = i
    else:
        best_score = math.inf
        for i in range(len(all_test_play_infos)):
            if all_test_play_infos[i]['score'] < best_score:
                best_score = all_test_play_infos[i]['score']
                best_test_play = i

    return all_test_play_infos[best_test_play]['coords']
