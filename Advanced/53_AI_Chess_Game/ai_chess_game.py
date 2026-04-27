from typing import List, Optional

class ChessAI:
    """Minimax AI Engine with Alpha-Beta Pruning."""
    def __init__(self, depth: int = 3):
        self._max_depth = depth

    def evaluate_board(self, state: int) -> int:
        # Mock evaluation: positive favors AI, negative favors opponent
        return state

    def minimax(self, state: int, depth: int, alpha: int, beta: int, is_maximizing: bool) -> int:
        if depth == 0: return self.evaluate_board(state)

        if is_maximizing:
            max_eval = -float('inf')
            # Mock moves: current_state + move_value
            for move in [5, 10, 15]: 
                eval = self.minimax(state + move, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha: break
            return max_eval
        else:
            min_eval = float('inf')
            for move in [-1, -2, -3]:
                eval = self.minimax(state + move, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha: break
            return min_eval
