from collections import deque
from typing import List, Tuple, Optional, Set

class AISnake:
    """
    AI Snake logic using Deque for body segments and BFS for pathfinding.
    """

    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self._snake: deque[Tuple[int, int]] = deque([(0, 0)])
        self._body_set: Set[Tuple[int, int]] = {(0, 0)}

    def find_path_to_food(self, food: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Uses BFS to find the shortest path to the food.
        Time Complexity: O(Rows * Cols)
        """
        head = self._snake[0]
        queue = deque([(head, [])])
        visited = {head} | self._body_set

        while queue:
            (r, c), path = queue.popleft()

            if (r, c) == food:
                return path

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self._rows and 0 <= nc < self._cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
        
        return None

    def move(self, next_pos: Tuple[int, int], is_food: bool) -> None:
        """Moves the snake to the next position."""
        self._snake.appendleft(next_pos)
        self._body_set.add(next_pos)
        if not is_food:
            tail = self._snake.pop()
            self._body_set.remove(tail)
