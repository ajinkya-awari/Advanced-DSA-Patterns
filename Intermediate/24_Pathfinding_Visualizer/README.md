# Pathfinding Visualizer (BFS/DFS)

### Architectural Overview
The **Pathfinding Visualizer** provides a comparative benchmarking suite for **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms within a 2D grid environment.

**Core Design Decisions:**
1.  **Algorithmic Optimality:** Demonstrates how BFS guarantees the shortest path in unweighted graphs by exploring in concentric layers.
2.  **Instrumentation Layer:** Captures real-time metrics including "Nodes Visited" and "Execution Time (ms)" to provide empirical performance data.
3.  **Path Reconstruction:** Employs a back-pointer dictionary to reconstruct the optimal route in $O(L)$ time once the destination is discovered.
4.  **LIFO vs FIFO Contrast:** Highlights the behavior differences between stack-based (DFS) and queue-based (BFS) frontier exploration.

### Complexity Analysis
- **BFS Search:** $O(V + E)$ where $V = Rows \times Cols$.
- **DFS Search:** $O(V + E)$.
- **Space:** $O(V)$ for visited sets and recursion/stack depth.
