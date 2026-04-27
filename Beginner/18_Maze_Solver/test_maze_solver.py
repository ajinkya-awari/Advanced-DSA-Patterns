import pytest
from maze_solver import MazeSolver, Coordinate

@pytest.fixture
def simple_maze():
    # 0 = path, 1 = wall
    return [
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 0]
    ]

def test_shortest_path_found(simple_maze):
    """Verify BFS finds the correct shortest path."""
    solver = MazeSolver(simple_maze)
    start = Coordinate(0, 0)
    end = Coordinate(2, 2)
    path = solver.find_shortest_path(start, end)
    
    assert len(path) == 5
    assert path[0] == start
    assert path[-1] == end

def test_no_path_available():
    """Verify behavior when destination is unreachable."""
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    solver = MazeSolver(grid)
    path = solver.find_shortest_path(Coordinate(0, 0), Coordinate(2, 2))
    assert path == []

def test_start_is_end():
    """Verify path when start and end are identical."""
    grid = [[0]]
    solver = MazeSolver(grid)
    start = Coordinate(0, 0)
    path = solver.find_shortest_path(start, start)
    assert path == [start]

def test_invalid_coordinates(simple_maze):
    """Verify exception handling for out-of-bounds inputs."""
    solver = MazeSolver(simple_maze)
    with pytest.raises(ValueError):
        solver.find_shortest_path(Coordinate(-1, 0), Coordinate(0, 0))

def test_multiple_paths_optimization():
    """Verify that BFS picks the shortest path among many."""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    solver = MazeSolver(grid)
    # Start (0,0) to (2,2) - multiple ways, but shortest is 5 steps (including start/end)
    path = solver.find_shortest_path(Coordinate(0, 0), Coordinate(2, 2))
    assert len(path) == 5

def test_empty_grid_prevention():
    """Verify validation for empty grids."""
    with pytest.raises(ValueError):
        MazeSolver([])
