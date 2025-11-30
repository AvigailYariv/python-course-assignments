
import helper


def init_board(rows, columns):
    """
    This function creates a new board.
    """
    if type(rows) != int or type(columns) != int or rows == 0 or columns == 0:
        return None
    board = []
    for i in range(rows):
        temp_row = []
        for j in range(columns):
            temp_row.append(helper.WATER)
        board.append(temp_row)
    return board


def cell_loc(name):
    """
    This function transfer the input letter of column and number of row, to coordinates.
    param name: can be only capital letter and a number.
    """
    column_letter = name[0]
    row_number = int(name[1:])  # this can be number with 2 numbers. like 10.
    column_num = ord(column_letter) - 65  # transfer letter to numbers. A == 0
    row_num = row_number - 1  # starts with 0.
    return (row_num, column_num)


def valid_ship(board, size, loc):
    """
    This function checks if a ship with a specific size can get into the board.
    """
    rows_num = len(board)
    columns_num = len(board[0])
    row = loc[0]
    col = loc[1]
    if row + size > rows_num or col >= columns_num:
        return False
    for i in range(size):
        if board[row + i][col] != helper.WATER:
            return False
    return True



def create_player_board(rows, columns, ship_sizes):
    ind = 0
    board = init_board(rows, columns)
    while ind < len(ship_sizes):
        helper.print_board(board)
        user_in = helper.get_input("please input coordinate for the top of the ship size " + str(ship_sizes[ind]) + ": ")
        if check_input(user_in):
            final_str = change_to_upper(user_in[0]) + user_in[1:]
            coor = cell_loc(final_str)
            if coor is not None and valid_ship(board, ship_sizes[ind], coor):
                for i in range(ship_sizes[ind]):
                    board[coor[0]+i][coor[1]] = helper.SHIP
                ind += 1
            else:
                print("you entered an invalid coordinate")
        else:
            print("you entered an invalid coordinate")
    return board


def fire_torpedo(board, loc):
    """
    This function changes the board by playing the game
    """
    row = loc[0]
    column = loc[1]
    if row >= len(board) or column >= len(board[0]):
        return board
    if board[row][column] == helper.WATER:
        board[row][column] = helper.HIT_WATER
    if board[row][column] == helper.SHIP:
        board[row][column] = helper.HIT_SHIP
    return board


def change_to_upper(letter):
    """
    This function change the letter to capital letter in case it wasn't.
    """
    if letter.isupper():
        return letter
    else:
        return letter.upper()


def check_input(user_input):
    """
    This function checks the input that the user enter when it's his turn to bump.
    """
    if (user_input[0].islower() or user_input[0].isupper()) and helper.is_int(user_input[1:]) and int(user_input[1:]) >= 0:
        return True
    return False


def list_of_locations_for_ships(board, ship_size):
    """
    This function returns a list of tuples. The tuples represent the locations that are empty.
    """
    locations = []
    max_row = len(board)-ship_size
    for i in range(len(board[0])):
        for j in range(max_row+1):
            for ind in range(ship_size):
                if board[j+ind][i] == helper.SHIP:
                    break
            else:
                locations.append((j, i))
    return locations


def list_of_locations_for_bump(board):
    """
    This function returns a list of tuples. The tuples represents the locations that are good for bump.
    """
    locations = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != helper.HIT_SHIP and board[i][j] != helper.HIT_WATER:
                locations.append((i, j))
    return locations


def hidden_board():
    """
    This function makes the board for the computer.
    """
    board = init_board(helper.NUM_ROWS, helper.NUM_COLUMNS)
    for ship in helper.SHIP_SIZES:
        loc_ship = helper.choose_ship_location(board, ship, list_of_locations_for_ships(board, ship))
        for i in range(ship):
            board[loc_ship[0]+i][loc_ship[1]] = helper.SHIP
    return board


def sum_sizes(ships_sizes):
    ans = 0
    for ship in ships_sizes:
        ans += ship
    return ans


def check_input_including_size_hidden(board, user_input):
    """
    This function checks the input including syntax and that the coordinates in the board.
    """
    if check_input(user_input):
        coor = cell_loc(change_to_upper(user_input))
        if coor is None:
            return False
        elif coor[0] < len(board) and coor[1] < len(board[0]) and board[coor[0]][coor[1]] != helper.HIT_SHIP and board[coor[0]][coor[1]] != helper.HIT_WATER:
            return True
        return False
    return False


def hit_point(visual_board, hidden_board, row, column):
    """
    This function change the visual board for the computer after a hit.
    """
    if hidden_board[row][column] == helper.WATER:
        visual_board[row][column] = helper.HIT_WATER
    if hidden_board[row][column] == helper.SHIP:
        visual_board[row][column] = helper.HIT_SHIP
    return visual_board


def count_bumps(board):
    """
    This function counts the amount of bumps in the board.
    """
    hits = 0
    for row in board:
        for sign in row:
            if sign == helper.HIT_SHIP:
                hits += 1
    return hits


def one_turn_player(board1, board2, computer_board, player_board):
    """
    This function operates 1 turn for the player.
    """
    user_bump = helper.get_input("choose a location for the torpedo bump: ")
    flag = check_input_including_size_hidden(board2, user_bump)
    while not flag:
        user_bump = helper.get_input("invalid value. \n choose a location for the torpedo bump: ")
        flag = check_input_including_size_hidden(board2, user_bump)
    upper_letter = change_to_upper(user_bump[0])
    final_str = upper_letter + user_bump[1:]
    row, column = cell_loc(final_str)
    board2 = hit_point(board2, computer_board, row, column)
    computer_board = fire_torpedo(computer_board, (row, column))
    target = helper.choose_torpedo_target(player_board, list_of_locations_for_bump(board1))
    player_board = hit_point(player_board, board1, target[0], target[1])
    board1 = fire_torpedo(board1, target)
    return board1, board2, player_board, computer_board



def run_single_game():
    """
    This function runs a single game of battleship
    """
    board1 = create_player_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)
    board2 = init_board(helper.NUM_ROWS, helper.NUM_COLUMNS)  # this is the visual board.
    computer_board = hidden_board()  # the board with the ships only.
    player_board = init_board(helper.NUM_ROWS, helper.NUM_COLUMNS)  # the hidden board for the player.
    hit_ship_1, hit_ship_2 = 0, 0
    sum_cor_ships = sum_sizes(helper.SHIP_SIZES)
    while hit_ship_1 < sum_cor_ships and hit_ship_2 < sum_cor_ships:  # while no one hit all of the ships.
        helper.print_board(board1, board2)
        board1, board2, player_board, computer_board = one_turn_player(board1, board2, computer_board, player_board)
        hit_ship_1, hit_ship_2 = count_bumps(board1), count_bumps(board2)
    helper.print_board(board1, computer_board)
    if hit_ship_1 < hit_ship_2:
        ask_another_game = helper.get_input("You won!! congrats! would you like to play another game? (Y/N): ")
    if hit_ship_1 > hit_ship_2:
        ask_another_game = helper.get_input("You lost :(  would you like to play another game? (Y/N): ")
    if hit_ship_1 == hit_ship_2:
        ask_another_game = helper.get_input("Even!! would you like to play another game? (Y/N): ")
    return ask_another_game


def main():
    ans = run_single_game()
    while ans == 'Y':
        ans = run_single_game()


if __name__ == "__main__":
    main()

