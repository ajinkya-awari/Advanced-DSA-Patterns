# Simple Text Editor (Stack)

### Architectural Overview
The **Simple Text Editor** is implemented using a **Command State Stack** to facilitate atomic document mutations and historical reversion.

**Core Design Decisions:**
1.  **State-Based Undo:** Before every mutation (append/delete), the current state is pushed onto the history stack. This allows `undo()` to be a constant-time reference revert.
2.  **Optimized Mutations:** Leverages Python's internal string handling for efficient concatenation and slicing.
3.  **Boundary Protection:** Enforces strict bounds checking for deletions and character retrievals, ensuring memory safety and runtime stability.
4.  **LIFO History:** Relies on the Last-In-First-Out property of the stack to ensure that reverts follow the exact reverse chronological order.

### Complexity Analysis
- **Append:** $O(N)$
- **Delete:** $O(N)$
- **Get (Peek):** $O(1)$
- **Undo:** $O(1)$
- **Space:** $O(N \times M)$ where $N$ is text size and $M$ is history depth.
