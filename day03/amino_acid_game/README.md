# Amino Acid Structure Learning Game 🎮

A simple educational game to help students learn to identify amino acids from their structural formulas.

## Setup

1. Install Python requirements:
```bash
pip install pillow
```

2. Add amino acid structure images:
   - Create PNG images for each amino acid structure
   - Name them exactly as follows (all lowercase):
     - alanine.png
     - arginine.png
     - asparagine.png
     - aspartic_acid.png
     - cysteine.png
     - glutamic_acid.png
     - glutamine.png
     - glycine.png
     - histidine.png
     - isoleucine.png
     - leucine.png
     - lysine.png
     - methionine.png
     - phenylalanine.png
     - proline.png
     - serine.png
     - threonine.png
     - tryptophan.png
     - tyrosine.png
     - valine.png
   - Place all images in the `images` folder

## Running the Game

```bash
python amino_acid_game.py
```

## How to Play

1. A structure image will be displayed
2. Type the name of the amino acid (e.g., "alanine")
3. Click Submit or press Enter to check your answer
4. Click Next to move to the next amino acid
5. Click Quit to end the game and see your final score

## Features

- Random selection of amino acids
- Score tracking
- Immediate feedback
- Case-insensitive answer checking
- Keyboard shortcuts (Enter to submit)
- Simple, clean interface

## Image Requirements

- Format: PNG
- Recommended size: 400x400 pixels or smaller (will be automatically resized if larger)
- Clear structural formula showing all atoms and bonds
- White or transparent background preferred

 ## Tests file

 - What the tests cover:

1. next_question returns a valid amino-acid key.
2. get_display_name returns the expected display string.
3. check_answer accepts full names, underscores/spaces, three-letter and one-letter codes (case-insensitive).
4. Incorrect answers decrease score and can make it negative.
5. Correct answers increase score.
6. A wrong-then-correct sequence adjusts score as expected.
7. Behavior when there's no active question returns an appropriate message

 ---

 ## Copilot instructions:
I need you to write me a Python program that creates a simple GUI game using tkinter. The game should test knowledge of the structure of amino acids. The program should randomly display structure of amino acid and ask the player to guess the name of the amino acid that have been shown. Include a "submit" button to check the answear and show a message like "Correct!" or "Try again" depending on the user's input. Include a Next button to show the next amino acid. The game should continue until the player chooses to quit. You can use RDKit to dw molecular structure but if it is better to download pictures of the amino acids - let me know and I will do it. The game should be in the amino_acid_game folder
