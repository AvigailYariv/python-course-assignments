
import sys
import random

NUM_ROWS = 10
NUM_COLUMNS = 8
SHIP_SIZES = (5, 5, 3, 3, 2, 2)

WATER = 0
SHIP = 1
HIT_WATER = 2
HIT_SHIP = 3

# Always use simple ASCII print — best compatibility
print_mapping = {
    WATER: '. ',
    SHIP: 'x ',
    HIT_WATER: 'o ',
    HIT_SHIP: '* ',
}
err_str = '? '

def str_row(board, i):
    if i < len(board):
        return (str(i+1).rjust(2) + ' ' +
                ''.join(print_mapping.get(board[i][j], err_str) for j in range(len(board[i]))))
    else:
        return ''

def print_board(board1, board2=None):
    boards = [board1] if board2 is None else [board1, board2]
    header = "   " + ''.join([chr(j + ord('A')) + ' ' for j in range(len(board1[0]))])
    sep = 10 * ' '
    print(*(header for _ in boards), sep=sep)

    for i in range(max(len(board) for board in boards)):
        print(*(str_row(board, i) for board in boards), sep=sep)

def get_input(msg):
    return input(msg)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def random_cell(cells):
    return random.choice(sorted(cells))

def choose_ship_location(board, size, locations):
    return random_cell(locations)

def choose_torpedo_target(board, locations):
    return random_cell(locations)

def seed(a):
    random.seed(a)
