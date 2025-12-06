import battleship
import helper

# -----------------------------
#  Tests for init_board
# -----------------------------
def test_init_board_valid():
    board = battleship.init_board(3, 4)
    assert len(board) == 3
    assert len(board[0]) == 4
    assert all(cell == helper.WATER for row in board for cell in row)

def test_init_board_invalid():
    assert battleship.init_board(0, 5) is None
    assert battleship.init_board(5, 0) is None
    assert battleship.init_board("A", 5) is None

# -----------------------------
#  Tests for cell_loc
# -----------------------------
def test_cell_loc():
    assert battleship.cell_loc("A1") == (0, 0)
    assert battleship.cell_loc("C5") == (4, 2)
    assert battleship.cell_loc("B10") == (9, 1)

# -----------------------------
#  Tests for valid_ship
# -----------------------------
def test_valid_ship():
    board = battleship.init_board(5, 5)
    assert battleship.valid_ship(board, 3, (0, 0)) is True
    assert battleship.valid_ship(board, 6, (0, 0)) is False     # overshoot
    board[1][0] = helper.SHIP                                    # block
    assert battleship.valid_ship(board, 3, (0, 0)) is False

# -----------------------------
#  Tests for fire_torpedo
# -----------------------------
def test_fire_torpedo_hit_and_miss():
    board = battleship.init_board(3, 3)
    board[1][1] = helper.SHIP

    # miss
    battleship.fire_torpedo(board, (0, 0))
    assert board[0][0] == helper.HIT_WATER

    # hit
    battleship.fire_torpedo(board, (1, 1))
    assert board[1][1] == helper.HIT_SHIP

# -----------------------------
#  Tests for change_to_upper
# -----------------------------
def test_change_to_upper():
    assert battleship.change_to_upper("a") == "A"
    assert battleship.change_to_upper("C") == "C"

# -----------------------------
#  Tests for check_input
# -----------------------------
def test_check_input():
    assert battleship.check_input("A5")
    assert battleship.check_input("c10")
    assert not battleship.check_input("AA5")  # too many letters
    assert not battleship.check_input("5A")   # wrong order
    assert not battleship.check_input("?5")   # invalid letter

# -----------------------------
#  Tests for list_of_locations_for_bump
# -----------------------------
def test_list_locations_for_bump():
    board = battleship.init_board(2, 2)
    board[0][0] = helper.HIT_WATER
    locs = battleship.list_of_locations_for_bump(board)
    assert (0, 0) not in locs
    assert (0, 1) in locs
    assert (1, 0) in locs
    assert (1, 1) in locs

# -----------------------------
#  Tests for sum_sizes
# -----------------------------
def test_sum_sizes():
    assert battleship.sum_sizes([5, 3, 2]) == 10
    assert battleship.sum_sizes([]) == 0
