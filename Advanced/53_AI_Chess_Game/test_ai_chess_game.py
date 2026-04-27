import pytest
from ai_chess_game import ChessAI

def test_alpha_beta_pruning():
    ai = ChessAI(depth=2)
    # Start at state 0. Maximizing AI will try to pick positive branches.
    score = ai.minimax(0, 2, -1000, 1000, True)
    assert score > 0
