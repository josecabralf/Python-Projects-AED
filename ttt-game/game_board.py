import pygame


class Board:

    """
    The Board class is a custom class that represents the game board for Tic Tac Toe. The class constructor initializes the Pygame module and sets up the game window. It also defines some colors used in the game. The Board class also contains a draw_board() method which draws the game board and the current state of the game using Pygame graphics.
    """

    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        # Set up the game window
        WINDOW_SIZE = (300, 300)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Tic Tac Toe")

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)

        # Set up the game board
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.font = pygame.font.Font(None, 50)

    def draw_board(self):
        """
        This function draws the Tic Tac Toe board on the screen and fills it with the color white. It then draws black lines to separate the board into nine sections, creating the 3x3 grid for the game.

        Next, it loops through each cell in the board and checks if it contains an "X" or "O" player mark. If the cell contains "X", the function creates a red text surface with the letter "X". If the cell contains "O", it creates a blue text surface with the letter "O". The function then calculates the x and y coordinates for the text based on the cell index, and blits the text onto the screen at that position.        
        """

        self.screen.fill(self.WHITE)
        pygame.draw.line(self.screen, self.BLACK, (100, 0), (100, 300), 5)
        pygame.draw.line(self.screen, self.BLACK, (200, 0), (200, 300), 5)
        pygame.draw.line(self.screen, self.BLACK, (0, 100), (300, 100), 5)
        pygame.draw.line(self.screen, self.BLACK, (0, 200), (300, 200), 5)
        for i in range(9):
            if self.board[i] == "X":
                text = self.font.render("X", True, self.RED)
            elif self.board[i] == "O":
                text = self.font.render("O", True, self.BLUE)
            else:
                continue
            x = (i % 3) * 100 + 30
            y = (i // 3) * 100 + 20
            self.screen.blit(text, (x, y))


def game_over(p):
    """
    The game_over() function is a utility function that checks if the game is over by checking for any three in a row of "X" or "O" or a tie. This function takes an instance of the Board class as a parameter and returns a boolean value indicating whether the game is over.
    """

    # Check rows
    for i in range(0, 9, 3):
        if p.board[i] == p.board[i+1] == p.board[i+2] and p.board[i] != " ":
            return True
    # Check columns
    for i in range(3):
        if p.board[i] == p.board[i+3] == p.board[i+6] and p.board[i] != " ":
            return True
    # Check diagonals
    if p.board[0] == p.board[4] == p.board[8] and p.board[0] != " ":
        return True
    if p.board[2] == p.board[4] == p.board[6] and p.board[2] != " ":
        return True
    # Check for a tie
    if " " not in p.board:
        return True
    return False


def get_winner(p):
    """
    The get_winner() function is another utility function that determines the winner of the game. It takes an instance of the Board class as a parameter and returns the winning player ("X" or "O") or "Tie" if the game is tied. If there is no winner and the game is not over, the function returns None.
    """

    # Check rows
    for i in range(0, 9, 3):
        if p.board[i] == p.board[i+1] == p.board[i+2] and p.board[i] != " ":
            return p.board[i]
    # Check columns
    for i in range(3):
        if p.board[i] == p.board[i+3] == p.board[i+6] and p.board[i] != " ":
            return p.board[i]
    # Check diagonals
    if p.board[0] == p.board[4] == p.board[8] and p.board[0] != " ":
        return p.board[0]
    if p.board[2] == p.board[4] == p.board[6] and p.board[2] != " ":
        return p.board[2]
    # Check if the self.board is full
    if " " not in p.board:
        return "Tie"
    # If no winner and the self.board is not full, return None
    return None
