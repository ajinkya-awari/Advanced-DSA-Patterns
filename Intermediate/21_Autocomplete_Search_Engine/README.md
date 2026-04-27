# Autocomplete Search Engine (Trie)

### Architectural Overview
The **Autocomplete Search Engine** is implemented using a **Trie (Prefix Tree)** to provide high-performance prefix matching and word discovery.

**Core Design Decisions:**
1.  **Prefix-Based Pathing:** Leverages common prefixes to share memory nodes, ensuring $O(L)$ insertion and discovery where $L$ is word length.
2.  **Deterministic Suffix Discovery:** Uses Depth-First Search (DFS) from a prefix node to gather all possible suggestions, ensuring that the suggestion set is exhaustive.
3.  **Enterprise Normalization:** All inputs are normalized to lowercase to ensure broad and consistent matching across mixed-case datasets.
4.  **Bulk-Insert Optimization:** Designed to handle large word sets ($1000+$) with minimal computational overhead through iterative pointer traversal.

### Complexity Analysis
- **Insert:** $O(L)$ where $L$ is word length.
- **Prefix Search:** $O(L + S)$ where $L$ is prefix length and $S$ is nodes in the matching subtree.
- **Space:** $O(N \times L)$ worst-case (no overlaps), significantly less with shared prefixes.
