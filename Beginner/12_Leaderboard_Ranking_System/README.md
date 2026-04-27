# Leaderboard Ranking System (Arrays / Sorting)

### Architectural Overview
The **Leaderboard Ranking System** maintains a sorted array of player records to provide efficient Top-K retrieval.

**Core Design Decisions:**
1.  **Sorted Array Invariant:** Maintains the list in descending order of scores using binary search insertion ($O(\log N)$ search, $O(N)$ shift).
2.  **Dual-Level Tie-Breaking:** Deterministically ranks players with identical scores by using their unique IDs as a secondary ascending sort criterion.
3.  **Registry-Backing:** Uses a Hash Map to track active scores, enabling $O(1)$ verification before attempting to update or remove a record.
4.  **Surgical Re-insertion:** Instead of re-sorting the entire dataset, the system only re-positions the specific player whose score has changed, minimizing computational overhead.

### Complexity Analysis
- **Update Score:** $O(N)$
- **Get Top-K:** $O(K)$
- **Get Rank:** $O(N)$
- **Space:** $O(N)$
