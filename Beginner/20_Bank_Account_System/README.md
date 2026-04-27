# Bank Account System (Linked List)

### Architectural Overview
The **Bank Account System** is implemented using a **Singly Linked List with a Tail Pointer** to maintain a chronological ledger of all financial transactions.

**Core Design Decisions:**
1.  **Tail Pointer Optimization:** By keeping a reference to the last node, the system achieves $O(1)$ time complexity for recording new transactions, ensuring high performance even as the ledger grows.
2.  **Immutable Ledger:** Transactions are stored as immutable `Transaction` dataclasses, preserving the integrity of the audit trail.
3.  **Atomic State Management:** Balance updates and historical records are coupled, ensuring that the current balance always reflects the sum of the ledger.
4.  **Overdraft Protection:** Strict validation prevents negative balances and ensures only positive currency values can be processed.

### Complexity Analysis
- **Deposit:** $O(1)$
- **Withdraw:** $O(1)$
- **Get History:** $O(N)$
- **Space:** $O(N)$
