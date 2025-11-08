# Amino Acid Structure Learning Game

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