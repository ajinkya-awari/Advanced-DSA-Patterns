# Browser History Manager (Doubly Linked List)

### Architectural Overview
The **Browser History Manager** is implemented using a **Doubly Linked List** to model the linear progression of web navigation.

**Core Design Decisions:**
1.  **Doubly Linked Nodes:** Each `HistoryNode` maintains pointers to both `prev` and `next` pages, enabling $O(1)$ pointer-based transitions during navigation.
2.  **Stateful Branching:** When `visit()` is called from a non-tail position (after navigating back), the entire "forward" history is truncated. This prevents memory leaks by allowing the Python garbage collector to reclaim unreachable nodes.
3.  **Boundary Safety:** Navigation methods (`back`, `forward`) are guarded against out-of-bounds requests, gracefully stopping at the earliest (Home) or latest page.

### Complexity Analysis
- **Visit:** $O(1)$
- **Back:** $O(Steps)$
- **Forward:** $O(Steps)$
- **Space:** $O(N)$
