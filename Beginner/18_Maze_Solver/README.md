# Maze Solver (BFS)

### Architectural Overview
The **Maze Solver** uses **Breadth-First Search (BFS)** to guarantee the shortest path in a 2D unweighted grid.

**Core Design Decisions:**
1.  **Layered Search:** Employs a FIFO Queue to explore the grid cell-by-cell in order of distance from the start.
2.  **Parent Backtracking:** Maintains a parent map to reconstruct the optimal route once the destination is reached.
3.  **Cycle Prevention:** Uses a visited set for $O(1)$ lookup, ensuring no cell is processed more than once.
4.  **Robust Bound Checking:** Validates all coordinates against grid dimensions and wall constraints before queuing.

### Complexity Analysis
- **Solve:** $O(V + E)$ where $V = Rows \times Cols$ and $E = 4V$ (4 directions).
- **Space:** $O(V)$ for the queue, visited set, and parent map.
