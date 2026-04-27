# Undo/Redo Feature (Stack)

### Architectural Overview
The **Undo/Redo Feature** is implemented using two discrete **Stacks** (LIFO structures) to manage state transitions in a text editor simulation.

**Core Design Decisions:**
1.  **Dual-Stack Architecture:** 
    -   `_undo_stack`: Stores previous states of the document.
    -   `_redo_stack`: Stores states that were "undone," allowing them to be restored unless a new mutation occurs.
2.  **State Persistence:** Every mutation (e.g., `write`) captures a snapshot of the current state before applying the change.
3.  **Redo Invalidation:** Following standard UX patterns, any new write operation clears the `_redo_stack` to prevent state divergence.

### Complexity Analysis
- **Write:** $O(N)$ (snapshotting current state)
- **Undo:** $O(1)$
- **Redo:** $O(1)$
- **Space:** $O(N \times M)$ where $N$ is state size and $M$ is history depth.
