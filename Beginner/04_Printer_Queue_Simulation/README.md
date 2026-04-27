# Printer Queue Simulation (Queue)

### Architectural Overview
The **Printer Queue Simulation** is implemented using a **Double-Ended Queue (Deque)** to model a First-In-First-Out (FIFO) scheduling system.

**Core Design Decisions:**
1.  **FIFO Principle:** Utilizes `collections.deque` for $O(1)$ enqueue (append) and dequeue (popleft) operations.
2.  **Job Persistence:** Maintains a history of completed jobs for audit and reporting purposes.
3.  **Strict Validation:** Enforces non-zero page counts and handles empty-queue exceptions to ensure system stability.

### Complexity Analysis
- **Add Job (Enqueue):** $O(1)$
- **Process Job (Dequeue):** $O(1)$
- **Cancel Job:** $O(N)$ (requires linear search and removal)
- **Space:** $O(N)$
