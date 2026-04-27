from collections import deque
from typing import List, Tuple, Optional, Dict, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    """Represents a position in the 2D grid."""
    row: int
    col: int

class MazeSolver:
    """
    Enterprise-grade Maze Solver using Breadth-First Search (BFS).
    
    Attributes:
        _grid (List[List[int]]): 2D grid where 0 is path and 1 is wall.
        _rows (int): Total rows in grid.
        _cols (int): Total columns in grid.
    """

    # Direction vectors for North, South, East, West
    _DIRECTIONS: Final[List[Tuple[int, int]]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def __init__(self, grid: List[List[int]]):
        if not grid or not grid[0]:
            raise ValueError("Grid cannot be empty.")
        self._grid = grid
        self._rows = len(grid)
        self._cols = len(grid[0])

    def find_shortest_path(self, start: Coordinate, end: Coordinate) -> List[Coordinate]:
        """
        Calculates the shortest path using BFS.
        
        Time Complexity: O(V + E) where V is total cells (Rows * Cols).
        Space Complexity: O(V) for the queue, visited set, and parent map.
        """
        # Input Validation
        if not self._is_valid(start) or not self._is_valid(end):
            raise ValueError("Start or End coordinate is out of bounds or a wall.")

        if start == end:
            return [start]

        queue: deque[Coordinate] = deque([start])
        visited: set[Coordinate] = {start}
        parent_map: Dict[Coordinate, Coordinate] = {}

        found = False
        while queue:
            current = queue.popleft()

            if current == end:
                found = True
                break

            for dr, dc in self._DIRECTIONS:
                neighbor = Coordinate(current.row + dr, current.col + dc)

                if (self._is_valid(neighbor) and 
                    neighbor not in visited and 
                    self._grid[neighbor.row][neighbor.col] == 0):
                    
                    visited.add(neighbor)
                    parent_map[neighbor] = current
                    queue.append(neighbor)

        return self._reconstruct_path(parent_map, start, end) if found else []

    def _is_valid(self, coord: Coordinate) -> bool:
        """Checks if a coordinate is within grid bounds."""
        return 0 <= coord.row < self._rows and 0 <= coord.col < self._cols

    def _reconstruct_path(self, parent_map: Dict[Coordinate, Coordinate], 
                         start: Coordinate, end: Coordinate) -> List[Coordinate]:
        """Backtracks from end to start to build the path list."""
        path = []
        current = end
        while current != start:
            path.append(current)
            current = parent_map[current]
        path.append(start)
        return path[::-1]
