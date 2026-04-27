import time
from collections import deque
from typing import List, Tuple, Optional, Dict, Final, Set
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    """Represents a coordinate in the grid."""
    row: int
    col: int

@dataclass
class SearchResult:
    """Metadata regarding an algorithm execution."""
    path: List[Point]
    nodes_visited: int
    execution_time_ms: float
    algorithm_name: str

class PathfindingVisualizer:
    """
    Enterprise-grade Pathfinding Engine comparing BFS and DFS.
    
    Grid Values: 0 = Path, 1 = Wall.
    """

    _DIRECTIONS: Final[List[Tuple[int, int]]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def __init__(self, grid: List[List[int]]):
        if not grid or not grid[0]:
            raise ValueError("Grid configuration cannot be empty.")
        self._grid = grid
        self._rows = len(grid)
        self._cols = len(grid[0])

    def _is_valid(self, p: Point) -> bool:
        return 0 <= p.row < self._rows and 0 <= p.col < self._cols and self._grid[p.row][p.col] == 0

    def solve_bfs(self, start: Point, end: Point) -> SearchResult:
        """
        Executes Breadth-First Search to find the shortest path.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        start_time = time.perf_counter()
        
        queue: deque[Point] = deque([start])
        visited: Set[Point] = {start}
        parent_map: Dict[Point, Point] = {}
        nodes_visited = 0

        found = False
        while queue:
            current = queue.popleft()
            nodes_visited += 1

            if current == end:
                found = True
                break

            for dr, dc in self._DIRECTIONS:
                neighbor = Point(current.row + dr, current.col + dc)
                if self._is_valid(neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    parent_map[neighbor] = current
                    queue.append(neighbor)

        path = self._reconstruct_path(parent_map, start, end) if found else []
        end_time = time.perf_counter()
        
        return SearchResult(
            path=path,
            nodes_visited=nodes_visited,
            execution_time_ms=(end_time - start_time) * 1000,
            algorithm_name="BFS"
        )

    def solve_dfs(self, start: Point, end: Point) -> SearchResult:
        """
        Executes Depth-First Search (Iterative with stack).
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        start_time = time.perf_counter()
        
        stack: List[Point] = [start]
        visited: Set[Point] = {start}
        parent_map: Dict[Point, Point] = {}
        nodes_visited = 0

        found = False
        while stack:
            current = stack.pop()
            nodes_visited += 1

            if current == end:
                found = True
                break

            for dr, dc in self._DIRECTIONS:
                neighbor = Point(current.row + dr, current.col + dc)
                if self._is_valid(neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    parent_map[neighbor] = current
                    stack.append(neighbor)

        path = self._reconstruct_path(parent_map, start, end) if found else []
        end_time = time.perf_counter()

        return SearchResult(
            path=path,
            nodes_visited=nodes_visited,
            execution_time_ms=(end_time - start_time) * 1000,
            algorithm_name="DFS"
        )

    def _reconstruct_path(self, parent_map: Dict[Point, Point], start: Point, end: Point) -> List[Point]:
        path = []
        current = end
        while current != start:
            path.append(current)
            current = parent_map[current]
        path.append(start)
        return path[::-1]
