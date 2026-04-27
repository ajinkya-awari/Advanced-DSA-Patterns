# File Compression Simulation (Huffman Coding)

### Architectural Overview
The **File Compression Simulation** uses the **Huffman Coding** algorithm to achieve lossless data compression via variable-length prefix-free encoding.

**Core Design Decisions:**
1.  **Greedy Tree Construction:** Leverages a **Min-Priority Queue** to build an optimal binary tree where higher frequency characters have shorter path lengths.
2.  **Prefix-Free Property:** Guarantees that no character's bit-code is a prefix of another, enabling deterministic $O(N)$ decoding.
3.  **Optimal Redundancy Reduction:** Uses frequency-based weighting to minimize the total bit-length of the encoded dataset.
4.  **Bit-String Simulation:** Operates on binary string representations to provide clear visibility into compression ratios and tree traversal logic.

### Complexity Analysis
- **Compression:** $O(N + K \log K)$ where $N$ is text length and $K$ is unique character count.
- **Decompression:** $O(N)$
- **Space:** $O(K)$ for the Huffman Tree.
