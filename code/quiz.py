import tkinter as tk
from tkinter import messagebox
import pygame
import math
import copy
from borders import *
import pygame as pg
import sys
import numpy as np
<<<<<<< HEAD
import math
import pygame
from pygame.time import Clock
from puzzle import Puzzle
from game import Game
import time
import random
=======
>>>>>>> 7106c72e6a72f2cc3d312d5f987e55a24ea796b9

class GameSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Selector")
        self.geometry("1032x622")

        # Load background image
        self.background_image = tk.PhotoImage(file="image.png")  # Replace "boy.png" with your image file
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_image_resized = self.background_image.subsample(3, 3)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_form()

    def create_form(self):
        self.form_label = tk.Label(self, text="Welcome to the Hero_Children Game Selector!", font=("Arial", 24, "bold"))
        self.form_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.name_label = tk.Label(self, text="Name:", font=("Arial", 16))
        self.name_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.name_entry = tk.Entry(self, font=("Arial", 16))
        self.name_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        self.age_label = tk.Label(self, text="Age:", font=("Arial", 16))
        self.age_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.age_entry = tk.Entry(self, font=("Arial", 16))
        self.age_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.submit_button = tk.Button(self, text="Submit", font=("Arial", 16), command=self.redirect_to_game_page)
        self.submit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def redirect_to_game_page(self):
        name = self.name_entry.get()
        age = self.age_entry.get()

        # Validate inputs
        if not name or not age:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return

        # Destroy current window
        self.destroy()

        # Redirect to game selection page
        game_selection_page = GameSelectionPage(name, age)
        game_selection_page.mainloop()

class GameSelectionPage(tk.Tk):
    def __init__(self, name, age):
        super().__init__()
        self.title("Game Selection")
        self.geometry("1032x622")

        # Load background image
        self.background_image = tk.PhotoImage(file="image.png")  # Replace "background_image.png" with your image file
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.name = name
        self.age = age

        self.create_game_buttons()

    def create_game_buttons(self):
        self.welcome_label = tk.Label(self, text=f"Hello, {self.name}!", font=("Arial", 14, "bold"))
        self.welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.game_label = tk.Label(self, text="Choose a game to play:")
        self.game_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        

        self.memory_card_button = tk.Button(self, text="PacMan", font=("Arial", 16), command=self.play_PacMan)
        self.memory_card_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.flag_matching_button = tk.Button(self, text="soduku", font=("Arial", 16), command=self.soduku)
        self.flag_matching_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.capital_guessing_button = tk.Button(self, text="puzzle", font=("Arial", 16), command=self.puzzle)
        self.capital_guessing_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.balloon_catching_button = tk.Button(self, text="Memory Card", font=("Arial", 16), command=self.MemoryCard)
        self.balloon_catching_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
#*********************************************************            PacMan                    ******************************************************************
    def play_PacMan(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 576
    
        def main():
            # Initialize all imported pygame modules
            pygame.init()
            # Set the width and height of the screen [width, height]
            screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
            # Set the current window caption
            pygame.display.set_caption("PACMAN")
            #Loop until the user clicks the close button.
            done = False
            # Used to manage how fast the screen updates
            clock = pygame.time.Clock()
            # Create a game object
            game = Game()
            # -------- Main Program Loop -----------
            while not done:
                # --- Process events (keystrokes, mouse clicks, etc)
                done = game.process_events()
                # --- Game logic should go here
                game.run_logic()
                # --- Draw the current frame
                game.display_frame(screen)
                # --- Limit to 30 frames per second
                clock.tick(30)
                #tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))
            # Close the window and quit.
            # If you forget this line, the program will 'hang'
            # on exit if running from IDLE.
            pygame.quit()

        if __name__ == '__main__':
            main()
# **************************************   end PacMan       *********************************************   

<<<<<<< HEAD
 
=======
# **************************************  start Soduku       *********************************************  
>>>>>>> 7106c72e6a72f2cc3d312d5f987e55a24ea796b9




<<<<<<< HEAD
 
    
# **************************************  start Soduku       ********************************************* 
=======
# **************************************   end Soduku       *********************************************   
    
# ***************            other game......    
>>>>>>> 7106c72e6a72f2cc3d312d5f987e55a24ea796b9
    def soduku(self):
        

        # Dimensions de la fenêtre et des cases
        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 700  # Ajuster la hauteur pour inclure la zone de message
        GRID_SIZE = 9
        CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

        # Dimensions de la zone de message
        MESSAGE_AREA_HEIGHT = 100
        MESSAGE_AREA_COLOR = (200, 200, 200)

        # Couleurs
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GRAY = (200, 200, 200)
        BLUE = (0, 0, 255)

        # Exemple de grille Sudoku (0 représente une case vide)
        EXAMPLE_BOARD = np.array([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])

        class SudokuGame:
            def __init__(self):
                self.grid = EXAMPLE_BOARD.copy()
                self.selected = None
                self.error_message = ""  # Initialiser le message d'erreur comme une chaîne vide
            def draw(self, screen):
                screen.fill(WHITE)
                # Dessiner la zone de jeu
                self.draw_board(screen)
                # Dessiner la zone de message
                self.draw_message_area(screen)
            def draw_board(self, screen):
                for i in range(GRID_SIZE + 1):
                    thickness = 4 if i % 3 == 0 else 1
                    pg.draw.line(screen, BLACK, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), thickness)
<<<<<<< HEAD
                    pg.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT - CELL_SIZE - MESSAGE_AREA_HEIGHT), thickness)
=======
                    pg.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT - CELL_SIZE), thickness)
>>>>>>> 7106c72e6a72f2cc3d312d5f987e55a24ea796b9
                for i in range(GRID_SIZE):
                    for j in range(GRID_SIZE):
                        value = self.grid[i][j]
                        if value != 0:
                            self.draw_number(screen, value, (j, i))
                if self.selected:
                    pg.draw.rect(screen, BLUE, (self.selected[0] * CELL_SIZE, self.selected[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
            def draw_message_area(self, screen):
                pg.draw.rect(screen, MESSAGE_AREA_COLOR, (0, SCREEN_HEIGHT - MESSAGE_AREA_HEIGHT, SCREEN_WIDTH, MESSAGE_AREA_HEIGHT))
                font = pg.font.Font(None, 25)
                text = font.render(self.error_message, True, BLUE)
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - MESSAGE_AREA_HEIGHT // 2))
                screen.blit(text, text_rect)
            def draw_number(self, screen, value, pos):
                font = pg.font.Font(None, 40)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(pos[0] * CELL_SIZE + CELL_SIZE // 2, pos[1] * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)
            def is_valid_move(self, value, pos):
                row, col = pos
                if value == 0:
                    return True
                # Check row
                if value in self.grid[row, :]:
                    return False
                # Check column
                if value in self.grid[:, col]:
                    return False
                # Check 3x3 grid
                start_row, start_col = (row // 3) * 3, (col // 3) * 3
                if value in self.grid[start_row:start_row + 3, start_col:start_col + 3]:
                    return False
                return True
            def input_number(self, number):
                if self.selected:
                    col, row = self.selected
                    if self.is_valid_move(number, (row, col)):
                        self.grid[row][col] = number
                        self.error_message = ""  
                    else:
                        self.error_message = "Mouvement invalide"
            def click(self, pos):
                if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT - MESSAGE_AREA_HEIGHT:
                    col = pos[0] // CELL_SIZE
                    row = pos[1] // CELL_SIZE
                    self.selected = (col, row)
                else:
                    self.selected = None
<<<<<<< HEAD
        def main():
=======
        if __name__ == '__main__':
>>>>>>> 7106c72e6a72f2cc3d312d5f987e55a24ea796b9
            pg.init()
            screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pg.display.set_caption("ARIJ Game")
            sudoku_game = SudokuGame()
            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        pos = pg.mouse.get_pos()
                        sudoku_game.click(pos)
                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_1:
                            sudoku_game.input_number(1)
                        elif event.key == pg.K_2:
                            sudoku_game.input_number(2)
                        elif event.key == pg.K_3:
                            sudoku_game.input_number(3)
                        elif event.key == pg.K_4:
                            sudoku_game.input_number(4)
                        elif event.key == pg.K_5:
                            sudoku_game.input_number(5)
                        elif event.key == pg.K_6:
                            sudoku_game.input_number(6)
                        elif event.key == pg.K_7:
                            sudoku_game.input_number(7)
                        elif event.key == pg.K_8:
                            sudoku_game.input_number(8)
                        elif event.key == pg.K_9:
                            sudoku_game.input_number(9)
                        elif event.key == pg.K_DELETE or event.key == pg.K_BACKSPACE:
                            sudoku_game.input_number(0)
                screen.fill(WHITE)
                sudoku_game.draw(screen)
                pg.display.flip()
            pg.quit()
            sys.exit()
<<<<<<< HEAD
        if __name__ == "__main__":
            main()
=======
>>>>>>> 7106c72e6a72f2cc3d312d5f987e55a24ea796b9
        messagebox.showinfo("Flag Matching Game", "You are playing Flag Matching Game. Click OK to finish the game.")

        # After playing the game, display score
        self.display_score()

# **************************************   end Soduku       *********************************************  


# **************************************   start puzzle      *********************************************  
    def puzzle(self):
        # Placeholder function for playing Capital Guessing Game
        

        pygame.init()
        pygame.font.init()
        SIZE = WIDTH, HEIGHT = (1000, 1000)

        BGCOLOR = (50, 50, 50)
        GFONT = pygame.font.SysFont("Comic Sans MS", 30)
        window = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
        pygame.display.set_caption('test')
        clock = Clock()

        p = Puzzle("image.jpg", (653, 980), (3, 3), (173, 10))
        p.scramble()

        def main():
            up = left = down = right = False
            
            running = True
            while running:
                clock.tick(60)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if p.moves_allowed():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                if not up:
                                    p.move_up()
                                    up = True
                            elif event.key == pygame.K_LEFT:
                                if not left:
                                    p.move_left()
                                    left = True
                            elif event.key == pygame.K_DOWN:
                                if not down:
                                    p.move_down()
                                    down = True
                            elif event.key == pygame.K_RIGHT:
                                if not right:
                                    p.move_right()
                                    right = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            up = False
                        elif event.key == pygame.K_LEFT:
                            left = False
                        elif event.key == pygame.K_DOWN:
                            down = False
                        elif event.key == pygame.K_RIGHT:
                            right = False

                window.fill(BGCOLOR)

                p.update()
                p.render(window)

                if p.is_solved():
                    p.reveal(window)

                pygame.display.update()

        if __name__ == '__main__':
            main()


        messagebox.showinfo("Capital Guessing Game", "You are playing Capital Guessing Game. Click OK to finish the game.")

        # After playing the game, display score
        self.display_score()
# **************************************   end puzzle      *********************************************

# **************************************   start MemoryCard     *********************************************
    def MemoryCard(self):
        # Placeholder function for playing Balloon Catching Game
        class MemoryCardGame:
            def __init__(self):
                self.data = ["A", "B", "C", "D", "E", "F", "G", "H"]
                self.data_length = len(self.data)
                self.game_end = 0
                self.dict_cards = {}
                self.clicked_cards = 0
                self.fst_ = None
                self.scnd_ = None
                self.start = time.time()

                self.root = tk.Tk()
                self.root.resizable(False,False)
                self.root.title("Memory Game")

                self.create_widgets()
                self.random_text()

            def create_widgets(self):
                f1 = tk.Frame(self.root)
                f1.pack()

                fonts = ['Helvetica', '20', 'bold']

                for i in range(16):
                    btn = tk.Button(f1, font=(fonts), width="5", height="3", command=lambda i=i: self.bttn_clicked(i))
                    btn.grid(row=i // 4, column=i % 4, padx=20, pady=40)
                    self.dict_cards[btn] = ""

            def random_text(self):
                occurances = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}
                for bttn in self.dict_cards:
                    if len(self.data) > 0:
                        random.shuffle(self.data)
                        x = self.data[0]
                        self.dict_cards[bttn] = x
                        occurances[x] = occurances[x] + 1
                        if occurances[x] == 2:
                            self.data.remove(x)

            def bttn_clicked(self, index):
                btn = list(self.dict_cards.keys())[index]
                self.clicked_cards += 1

                if self.clicked_cards == 1:
                    self.fst_ = btn
                    btn.configure(text=self.dict_cards[btn], state=tk.DISABLED)
                elif self.clicked_cards == 2:
                    self.scnd_ = btn
                    btn.configure(text=self.dict_cards[btn], state=tk.DISABLED)
                    self.root.after(500, self.check_same)

            def check_same(self):
                if self.scnd_['text'] != self.fst_['text']:
                    self.fst_.configure(text="", state="normal")
                    self.scnd_.configure(text="", state="normal")
                else:
                    self.game_end += 1

                if self.game_end == self.data_length:
                    messagebox.showinfo("MEMORY GAME", "You have spent " + str(int(time.time() - self.start)) + " sec!")
                    self.root.destroy()

                self.clicked_cards = 0

            def play(self):
                self.root.mainloop()

        # Run the game
        if __name__ == "__main__":
            game = MemoryCardGame()
            game.play()
        messagebox.showinfo("Balloon Catching Game", "You are playing Balloon Catching Game. Click OK to finish the game.")

        # After playing the game, display score
        self.display_score()
# **************************************   end MemoryCard     *********************************************

    def display_score(self):
        # Placeholder function to display score
        score = 50  # Placeholder score, you can replace it with actual score
        messagebox.showinfo("Score", f"Your score is: {score}")

if __name__ == "__main__":
    app = GameSelector()
    app.mainloop()