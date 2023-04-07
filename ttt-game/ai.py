from game_board import get_winner


def minimax(b, depth, is_maximizing):
    """This function is used to evaluate all possible moves in the game tree and choose the best move for the AI.
        Parameters:
            b: an instance of the Board class, representing the current state of the game board.
            depth: an integer representing the current depth of the game tree.
            is_maximizing: a boolean value indicating whether the function is currently maximizing or minimizing the score.
        Returns:
            The score of the best move, calculated using the minimax algorithm."""

    # Check if the game is over
    winner = get_winner(b)
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
            if b.board[i] == " ":
                b.board[i] = "O"
                score = minimax(b, depth + 1, False)
                b.board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if b.board[i] == " ":
                b.board[i] = "X"
                score = minimax(b, depth + 1, True)
                b.board[i] = " "
                best_score = min(best_score, score)
        return best_score


def get_ai_move(b):
    """This function chooses the best move for the AI by calling the minimax function for all possible moves and selecting the move with the highest score.
    Parameters:
        b: an instance of the Board class, representing the current state of the game board.
    Returns:
        The index of the best move for the AI, as an integer."""

    # Choose the best move using the minimax algorithm
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if b.board[i] == " ":
            b.board[i] = "O"
            score = minimax(b, 0, False)
            b.board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
