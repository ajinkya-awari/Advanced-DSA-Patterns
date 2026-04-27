# Student Record System (Arrays)

### Architectural Overview
The **Student Record System** is implemented using a high-performance, fixed-capacity array simulation to demonstrate low-level memory management and index-based data manipulation.

**Core Design Decisions:**
1.  **Contiguous Memory Simulation:** Uses a pre-allocated Python list to simulate a static array. This ensures $O(1)$ access times by index but requires manual management of the `occupancy_count`.
2.  **ID-Based Indexing:** Employs a private `_find_index` method using linear search ($O(N)$) as the primary mechanism for locating records, ensuring data integrity before any mutation.
3.  **Optimal Deletion:** Implements a manual shift-left operation during deletion. While this is $O(N)$ in the worst case, it maintains the contiguous nature of the array, preventing "holes" in data and ensuring subsequent operations remain predictable.
4.  **Validation Layer:** Enforces strict type checking and existence validation to prevent duplicate IDs or corrupted records, typical of enterprise-grade entity management systems.

### Complexity Analysis
- **Create:** $O(N)$ (due to uniqueness check)
- **Read:** $O(N)$ (linear search by ID)
- **Update:** $O(N)$
- **Delete:** $O(N)$ (shifting elements)
- **Space:** $O(Capacity)$
