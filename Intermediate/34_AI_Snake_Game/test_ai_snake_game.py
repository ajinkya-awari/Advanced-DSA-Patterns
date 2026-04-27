import pytest
from ai_snake_game import AISnake

def test_snake_pathfinding():
    snake = AISnake(5, 5)
    path = snake.find_path_to_food((2, 2))
    assert path is not None
    assert len(path) == 4 # (0,1), (0,2), (1,2), (2,2) or similar
    assert path[-1] == (2, 2)

def test_snake_collision_avoidance():
    snake = AISnake(3, 3)
    # Block path
    snake.move((0, 1), False)
    snake.move((1, 1), False)
    path = snake.find_path_to_food((2, 1))
    assert path[0] != (1, 1) # Must not pass through body
