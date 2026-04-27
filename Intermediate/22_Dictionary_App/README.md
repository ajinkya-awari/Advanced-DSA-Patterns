# Dictionary App (HashMap and Trie)

### Architectural Overview
The **Dictionary App** leverages a hybrid data architecture to provide optimal performance for two distinct search paradigms: exact lookup and prefix-based discovery.

**Core Design Decisions:**
1.  **Dual-Structure Pattern:** Combines a **Hash Map** for $O(1)$ definition retrieval with a **Trie** for $O(L)$ autocomplete suggestions.
2.  **Stateless Normalization:** Implements a strict normalization layer (lower-casing, trimming) to ensure data integrity across both structures.
3.  **Recursive Discovery:** Uses Depth-First Search (DFS) on the Trie sub-tree to collect all word suffixes for a given prefix.
4.  **Synchronized Mutations:** Word additions and deletions are mirrored across both structures to maintain systemic consistency.

### Complexity Analysis
- **Add Word:** $O(L)$ where $L$ is word length.
- **Get Definition:** Average $O(1)$.
- **Suggest Words:** $O(L + K)$ where $K$ is total nodes in the prefix sub-tree.
- **Space:** $O(N \times L)$ due to dual-storage.
