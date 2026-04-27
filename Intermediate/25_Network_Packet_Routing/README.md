# Network Packet Routing (Graph)

### Architectural Overview
The **Network Packet Routing System** uses a **Weighted Directed Graph** and **Dijkstra's Algorithm** to determine the most efficient path for data transmission across a topology of routers.

**Core Design Decisions:**
1.  **Efficiency Invariant:** Employs Dijkstra with a binary heap priority queue to ensure $O((V+E) \log V)$ performance, making it robust for complex enterprise networks.
2.  **Latency-Aware Routing:** Factors in per-link latency (edge weights) to prioritize the path of least cost rather than just the fewest hops.
3.  **Adjacency List Model:** Optimizes space complexity to $O(V + E)$, allowing for sparse network representations with thousands of routers.
4.  **Path Reconstruction:** Dynamically builds the route hops from a predecessor map, ensuring linear-time path retrieval.

### Complexity Analysis
- **Find Route:** $O((V + E) \log V)$ where $V$ is routers and $E$ is links.
- **Add Link:** $O(1)$.
- **Space:** $O(V + E)$ for adjacency list and priority queue.
