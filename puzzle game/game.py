import tkinter as tk
import random
from tkinter import messagebox

# Constants
GRID_SIZE = 4  # 4x4 grid
NUM_PAIRS = (GRID_SIZE * GRID_SIZE) // 2  # Total number of pairs
TIME_LIMIT = 60  # 60 seconds

class MemoryPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        
        self.buttons = []  # To hold button references
        self.cards = []
        self.flipped_cards = []  # To store currently flipped cards
        self.matched_cards = 0
        self.time_left = TIME_LIMIT
        
        self.setup_game()
        self.start_timer()

    def setup_game(self):
        # Generate pairs of symbols (emojis or letters)
        symbols = list("🍎🍌🍒🍇🍓🍍🥭🍑") * 2
        random.shuffle(symbols)
        
        self.cards = symbols
        self.flipped_cards = []
        self.matched_cards = 0
        
        # Setup the grid of buttons (cards)
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                btn = tk.Button(self.root, text=" ", width=6, height=3, font=("Arial", 20),
                                command=lambda x=i, y=j: self.flip_card(x, y))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

        # Create a label for the timer
        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left} seconds", font=("Arial", 16))
        self.timer_label.grid(row=GRID_SIZE, column=0, columnspan=GRID_SIZE)

    def flip_card(self, x, y):
        # Do nothing if the card is already flipped or matched
        if self.buttons[x][y]['text'] != " ":
            return

        # Show the card
        self.buttons[x][y].config(text=self.cards[x * GRID_SIZE + y])

        # Add the card to the list of flipped cards
        self.flipped_cards.append((x, y))

        # If two cards are flipped, check for a match
        if len(self.flipped_cards) == 2:
            self.root.after(500, self.check_match)  # Wait for 500ms to show the cards

    def check_match(self):
        (x1, y1), (x2, y2) = self.flipped_cards
        
        # Check if the two flipped cards match
        if self.cards[x1 * GRID_SIZE + y1] == self.cards[x2 * GRID_SIZE + y2]:
            self.buttons[x1][y1].config(bg="lightgreen", state="disabled")
            self.buttons[x2][y2].config(bg="lightgreen", state="disabled")
            self.matched_cards += 2
        else:
            self.buttons[x1][y1].config(text=" ")
            self.buttons[x2][y2].config(text=" ")

        self.flipped_cards = []  # Reset flipped cards

        # Check if the player has matched all the cards
        if self.matched_cards == GRID_SIZE * GRID_SIZE:
            self.end_game(True)

    def start_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            self.root.after(1000, self.start_timer)
        else:
            self.end_game(False)

    def end_game(self, won):
        if won:
            messagebox.showinfo("Congratulations", "You won! You matched all the cards!")
        else:
            messagebox.showinfo("Game Over", "Time's up! You didn't match all the cards.")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()
