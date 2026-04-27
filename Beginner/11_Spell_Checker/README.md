# Spell Checker (Hashing)

### Architectural Overview
The **Spell Checker** is implemented using a custom **Chained Hash Table** to demonstrate advanced collision resolution and dynamic memory management.

**Core Design Decisions:**
1.  **Polynomial Rolling Hash:** Uses a prime-base multiplier to ensure uniform distribution of keys across buckets, minimizing primary clustering.
2.  **Collision Resolution (Chaining):** Employs linked lists within buckets to handle hash collisions efficiently, maintaining system performance under high load.
3.  **Dynamic Rehashing:** Implements an automatic $2 \times$ capacity expansion when the load factor exceeds 0.75, ensuring average $O(1)$ lookup performance.
4.  **Case-Insensitive Normalization:** Ensures robust lookups by normalizing all inputs to lowercase and stripping whitespace.

### Complexity Analysis
- **Insert:** Amortized $O(L)$ where $L$ is word length ($O(N)$ during resize).
- **Lookup:** Average $O(L)$, Worst-case $O(N)$.
- **Space:** $O(N + K)$ where $N$ is word count and $K$ is bucket capacity.
