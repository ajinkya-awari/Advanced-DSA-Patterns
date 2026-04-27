# Basic Library Management (Arrays)

### Architectural Overview
The **Basic Library Management System** is implemented using a **Contiguous Array** structure to manage physical book records and their availability states.

**Core Design Decisions:**
1.  **ISBN Uniqueness:** Enforces a strict one-to-one mapping between ISBN and record, preventing catalog duplication.
2.  **State Management:** Tracks `is_checked_out` status with robust error handling to prevent illegal state transitions (e.g., checking out an already borrowed book).
3.  **Contiguous Deletion:** Repairs the array using left-shift operations when a book is removed, ensuring that the catalog remains dense and indexable.
4.  **Memory Constraints:** Implements a fixed-capacity model to simulate hardware-constrained environments typical of embedded library kiosk systems.

### Complexity Analysis
- **Add Book:** $O(N)$
- **Checkout/Return:** $O(N)$
- **Remove Book:** $O(N)$
- **Space:** $O(Capacity)$
