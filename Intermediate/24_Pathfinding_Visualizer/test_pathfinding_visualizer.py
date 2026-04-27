import pytest
from pathfinding_visualizer import PathfindingVisualizer, Point

@pytest.fixture
def large_grid():
    # 10x10 grid with a middle wall
    grid = [[0 for _ in range(10)] for _ in range(10)]
    for r in range(1, 9):
        grid[r][5] = 1 # Vertical wall
    return grid

def test_bfs_shortest_path():
    """Verify that BFS always finds the optimal path."""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    viz = PathfindingVisualizer(grid)
    start, end = Point(0, 0), Point(2, 2)
    
    result = viz.solve_bfs(start, end)
    # Shortest path in this 3x3 with middle wall is 5 steps
    assert len(result.path) == 5
    assert result.algorithm_name == "BFS"

def test_dfs_non_optimal_path():
    """Verify that DFS finds a path but potentially not the shortest."""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    viz = PathfindingVisualizer(grid)
    start, end = Point(0, 0), Point(2, 2)
    
    result = viz.solve_dfs(start, end)
    assert len(result.path) >= 5 # Might be longer due to stack behavior
    assert result.path[-1] == end

def test_unreachable_target():
    """Verify behavior when path is blocked."""
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    viz = PathfindingVisualizer(grid)
    start, end = Point(0, 0), Point(2, 2)
    
    assert viz.solve_bfs(start, end).path == []
    assert viz.solve_dfs(start, end).path == []

def test_performance_comparison(large_grid):
    """Benchmarks execution metrics between BFS and DFS."""
    viz = PathfindingVisualizer(large_grid)
    start, end = Point(0, 0), Point(9, 9)
    
    bfs_res = viz.solve_bfs(start, end)
    dfs_res = viz.solve_dfs(start, end)
    
    # BFS must be <= DFS path length (optimality)
    assert len(bfs_res.path) <= len(dfs_res.path)
    # Output metrics for verification
    print(f"\nBFS Visited: {bfs_res.nodes_visited}, Time: {bfs_res.execution_time_ms:.4f}ms")
    print(f"DFS Visited: {dfs_res.nodes_visited}, Time: {dfs_res.execution_time_ms:.4f}ms")
