# Blockchain Simulation (Linked List + Hashing)

### Architectural Overview
The **Blockchain Simulation** implements a decentralized, immutable ledger using a **Hash-Linked List** data structure. Each block encapsulates a transaction payload and a cryptographic link to its predecessor, ensuring a tamper-evident chain of custody.

**Core Design Decisions:**
1.  **Hash-Based Linkage:** Each node (Block) stores the SHA-256 hash of the previous node. Any modification to a previous block invalidates the entire subsequent chain.
2.  **Deterministic Integrity Scanning:** Implements a linear $O(N)$ validation algorithm that cross-references stored hashes with real-time payload recalculations.
3.  **Genesis Block Protocol:** Enforces a hardcoded origin point to serve as the immutable anchor for the ledger.

### Complexity Analysis
- **Add Block:** $O(1)$
- **Integrity Validation:** $O(N)$
- **Space:** $O(N)$

---

### 🛡️ Challenges Encountered
A key engineering hurdle was ensuring that the `is_chain_valid` method accurately detected data tampering at any point in the history. I implemented a dual-check system: first, validating the block's own hash against its contents, and second, verifying that the current block's `prev_hash` pointer matched the actual hash of the previous block. This ensures $100\%$ detection of both content mutations and linkage corruption.
