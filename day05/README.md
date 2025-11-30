**🚢 Battleship – Python Console Game**
---
This project is an implementation of the classic game Battleship

The game allows a human player to place ships on a board and play against a computer opponent. Each turn, both the player and the computer fire torpedoes at each other until one side hits all opponent ships.

*▶️ How to Run the Game*
---
The game uses only the Python standard library — no external dependencies.

1. Make sure you have Python 3 installed

Check using:

python3 --version

2. Run the game
python3 battleship.py


The game will start immediately. You will be asked to:

Place your ships on the board

Fire torpedoes at the computer board

Continue rounds until someone wins

Choose whether to play again

*🎮 How to Play*
---
1. Placing Your Ships

You will be asked to enter coordinates like:

A3
C7


The letter is the column (A, B, C …)
The number is the row (1, 2, 3 …)

Ships are always placed vertically (downwards).

If you enter an invalid coordinate, you will be asked to try again.

2. Firing Torpedoes

During each turn:

You choose a location to attack (same coordinate format)

The game updates your hit/miss on the computer board

The computer chooses a location randomly to attack your board

The game ends when all ships of one side have been destroyed.

*🧪 About the Tests*
---

This project includes automated tests that check whether the functions in the game work correctly.
These tests were written with the help of AI.

You can run the tests with:

python -m pytest


✔️ What the tests check

The tests focus on the logic in battleship.py, and include checks such as:

1. Board initialization

2. Coordinate handling

3. Ship placement

4. Gameplay mechanics

5. Computer logic

These tests ensure the game logic is correct and consistent.

*Note:*
---

I used AI only to help generate the test files, not for writing my game logic.
