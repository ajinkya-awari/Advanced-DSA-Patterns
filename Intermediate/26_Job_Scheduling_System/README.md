# Job Scheduling System (Priority Queue)

### Architectural Overview
The **Job Scheduling System** is implemented using a **Max-Priority Queue** (Binary Heap) to ensure that the highest-priority tasks are executed first.

**Core Design Decisions:**
1.  **Heap-Based Scheduling:** Leverages a binary heap to maintain $O(\log N)$ submission and extraction efficiency.
2.  **FIFO Tie-Breaking:** Integrates a sequence counter to ensure deterministic First-In-First-Out behavior for jobs with identical priority levels.
3.  **Lazy Deletion Strategy:** Employs a hash-backed registry for job cancellations, allowing $O(1)$ removal marking with $O(\log N)$ cleanup during extraction.
4.  **Max-Heap Simulation:** Negates priority values to utilize the standard min-heap implementation for max-priority scheduling logic.

### Complexity Analysis
- **Schedule Job:** $O(\log N)$
- **Fetch Next Job:** Amortized $O(\log N)$
- **Cancel Job:** $O(1)$
- **Space:** $O(N)$ for heap and registry storage.
