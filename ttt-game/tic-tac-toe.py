import pygame


# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_SIZE = (300, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the game board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
font = pygame.font.Font(None, 50)

# Set up the AI player


def minimax(board, depth, is_maximizing):
    # Check if the game is over
    winner = get_winner(board)
    if winner is not None:
        if winner == "O":
            return 10 - depth
        elif winner == "X":
            return depth - 10
        else:
            return 0
    # If the game is not over, recursively evaluate all possible moves
    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def get_ai_move(board):
    # Choose the best move using the minimax algorithm
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


# Define a function to draw the game board


def draw_board():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)
    for i in range(9):
        if board[i] == "X":
            text = font.render("X", True, RED)
        elif board[i] == "O":
            text = font.render("O", True, BLUE)
        else:
            continue
        x = (i % 3) * 100 + 30
        y = (i // 3) * 100 + 20
        screen.blit(text, (x, y))

# Define a function to check if the game is over


def game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        return True
    # Check for a tie
    if " " not in board:
        return True
    return False


def get_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]
    # Check if the board is full
    if " " not in board:
        return "Tie"
    # If no winner and the board is not full, return None
    return None


# Set up the game loop
running = True
turn = "X"
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and turn == "X" and not game_over():
            pos = pygame.mouse.get_pos()
            col = pos[0] // 100
            row = pos[1] // 100
            index = row * 3 + col
            if board[index] == " ":
                # Set the user's move on the board
                board[index] = turn
                # Draw the updated board
                draw_board()
                # Check if the game is over
                if game_over():
                    winner = get_winner(board)
                    if winner != 'Tie':
                        print(f"{winner} won the game!")
                    else:
                        print("It's a tie!")
                    continue
                # Switch turns
                turn = "O"
        elif turn == "O" and not game_over():
            # Get the AI's move
            move = get_ai_move(board)
            # Set the AI's move on the board
            board[move] = turn
            # Draw the updated board
            draw_board()
            # Check if the game is over
            if game_over():
                winner = get_winner(board)
                if winner != 'Tie':
                    print(f"{winner} won the game!")
                else:
                    print("It's a tie!")
                continue
            # Switch turns
            turn = "X"
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
