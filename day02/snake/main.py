"""
Simple Snake game using tkinter.

Controls:
 - Arrow keys to move the snake
 - 'r' to restart when game over
 - 'q' or window close to quit

Run:
 python main.py

This file is intentionally self-contained and uses only the Python standard library.
"""

import tkinter as tk
import random


CELL_SIZE = 20  # pixels
GRID_WIDTH = 30  # cells
GRID_HEIGHT = 20  # cells
DELAY = 120  # milliseconds between moves (smaller = faster)


class SnakeGame(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.master.title("Snake")
		self.pack()

		self.canvas = tk.Canvas(self, width=CELL_SIZE * GRID_WIDTH, height=CELL_SIZE * GRID_HEIGHT, bg="black")
		self.canvas.pack()

		self.score_var = tk.IntVar(value=0)
		score_frame = tk.Frame(self)
		score_frame.pack(fill="x")
		tk.Label(score_frame, text="Score:", font=("Arial", 12)).pack(side="left", padx=(6,0))
		tk.Label(score_frame, textvariable=self.score_var, font=("Arial", 12)).pack(side="left")

		self.reset_game()

		# Bind keys
		self.master.bind("<Up>", lambda e: self.change_direction((0, -1)))
		self.master.bind("<Down>", lambda e: self.change_direction((0, 1)))
		self.master.bind("<Left>", lambda e: self.change_direction((-1, 0)))
		self.master.bind("<Right>", lambda e: self.change_direction((1, 0)))
		self.master.bind("r", lambda e: self.reset_game())
		self.master.protocol("WM_DELETE_WINDOW", self.on_close)

		self.running = True
		self.after_id = None
		self.loop()

	def reset_game(self):
		# Initialize snake in the middle
		mid_x = GRID_WIDTH // 2
		mid_y = GRID_HEIGHT // 2
		self.snake = [(mid_x, mid_y), (mid_x - 1, mid_y), (mid_x - 2, mid_y)]
		self.direction = (1, 0)  # moving right
		self.place_food()
		self.score_var.set(0)
		self.game_over = False
		self.draw()

	def place_food(self):
		free_cells = {(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)} - set(self.snake)
		if not free_cells:
			self.food = None
			return
		self.food = random.choice(list(free_cells))

	def change_direction(self, new_dir):
		if self.game_over:
			return
		# Prevent reversing
		dx, dy = new_dir
		cdx, cdy = self.direction
		if (dx, dy) == (-cdx, -cdy):
			return
		self.direction = (dx, dy)

	def loop(self):
		if not self.running:
			return
		if not self.game_over:
			self.update_snake()
			self.draw()
			self.after_id = self.after(DELAY, self.loop)
		else:
			# show game over text
			self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height()//2,
									text=f"GAME OVER\nScore: {self.score_var.get()}\nPress 'r' to restart",
									fill="white", font=("Arial", 18), justify="center")

	def update_snake(self):
		head_x, head_y = self.snake[0]
		dx, dy = self.direction
		new_head = (head_x + dx, head_y + dy)

		# Check collisions with walls
		x, y = new_head
		if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
			self.game_over = True
			return

		# Check collision with self
		if new_head in self.snake:
			self.game_over = True
			return

		# Move snake
		self.snake.insert(0, new_head)

		# Check food
		if self.food and new_head == self.food:
			self.score_var.set(self.score_var.get() + 1)
			self.place_food()
		else:
			self.snake.pop()

	def draw(self):
		self.canvas.delete("all")

		# Draw food
		if self.food:
			x, y = self.food
			self.draw_cell(x, y, "red")

		# Draw snake
		for i, (x, y) in enumerate(self.snake):
			color = "green" if i == 0 else "lime"
			self.draw_cell(x, y, color)

	def draw_cell(self, x, y, color):
		x1 = x * CELL_SIZE
		y1 = y * CELL_SIZE
		x2 = x1 + CELL_SIZE
		y2 = y1 + CELL_SIZE
		self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

	def on_close(self):
		self.running = False
		if self.after_id:
			self.after_cancel(self.after_id)
		self.master.destroy()


def main():
	root = tk.Tk()
	game = SnakeGame(root)
	root.mainloop()


if __name__ == "__main__":
	main()

