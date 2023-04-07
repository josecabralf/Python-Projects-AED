import pygame
from game_board import Board
from game_board import get_winner, game_over
from ai import get_ai_move

"""
  This module is the main driver program for a Tic Tac Toe game. It imports pygame for graphical display, Board class from game_board module for the game board and get_winner and game_over functions from game_board module for checking if the game is over, and get_ai_move function from ai module for getting the AI's move.
"""


def main():
    """
    The main function initializes the game board, sets up a game loop, and handles events. The game loop runs while running is true, and switches between the user's turn and the AI's turn until the game is over or the user exits the game.

    During the user's turn, the pygame.MOUSEBUTTONUP event is handled to get the user's move, set the move on the board, draw the updated board, check if the game is over, and switch turns. During the AI's turn, the get_ai_move function is called to get the AI's move, set the move on the board, draw the updated board, check if the game is over, and switch turns.

    When the game is over, the winner is determined using get_winner function and a message is printed to the console. Finally, the pygame is quit and the game is closed.
    """

    # Set up the game loop
    b = Board()
    running = True
    turn = "X"
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and turn == "X" and not game_over(b):
                pos = pygame.mouse.get_pos()
                col = pos[0] // 100
                row = pos[1] // 100
                index = row * 3 + col
                if b.board[index] == " ":
                    # Set the user's move on the b
                    b.board[index] = turn
                    # Draw the updated b
                    b.draw_board()
                    # Check if the game is over
                    if game_over(b):
                        winner = get_winner(b)
                        if winner != 'Tie':
                            print(f"{winner} won the game!")
                        else:
                            print("It's a tie!")
                        continue
                    # Switch turns
                    turn = "O"
            elif turn == "O" and not game_over(b):
                # Get the AI's move
                move = get_ai_move(b)
                # Set the AI's move on the b
                b.board[move] = turn
                # Draw the updated b
                b.draw_board()
                # Check if the game is over
                if game_over(b):
                    winner = get_winner(b)
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


if __name__ == "__main__":
    main()
