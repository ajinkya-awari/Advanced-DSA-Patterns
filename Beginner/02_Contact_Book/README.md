# Contact Book (Linked List)

### Architectural Overview
The **Contact Book** is implemented as a **Singly Linked List** to demonstrate dynamic memory allocation and pointer-based data structures.

**Core Design Decisions:**
1.  **Node-Based Architecture:** A custom `ContactNode` class encapsulates the `Contact` entity and a reference to the next node, forming the backbone of the linear structure.
2.  **O(1) Insertion:** New contacts are prepended to the head of the list. This ensures constant-time insertion regardless of the book's size.
3.  **Linear Search Path:** Search and Deletion operations follow an $O(N)$ traversal pattern. While less efficient than hash-based lookups, it strictly adheres to the requested Linked List paradigm.
4.  **Robust Deletion:** The deletion logic handles edge cases such as empty lists, head deletions, and middle/tail deletions while maintaining pointer integrity.

### Complexity Analysis
- **Insert (Head):** $O(1)$
- **Search (Name):** $O(N)$
- **Update:** $O(N)$
- **Delete:** $O(N)$
- **Space:** $O(N)$
