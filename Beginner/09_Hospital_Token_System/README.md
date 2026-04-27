# Hospital Token System (Queue)

### Architectural Overview
The **Hospital Token System** uses a **FIFO Queue** to manage sequential patient consultations in a clinic.

**Core Design Decisions:**
1.  **Sequential Token Generation:** Ensures a unique, increasing identifier for every patient to prevent triage disputes.
2.  **$O(1)$ Operations:** Uses `collections.deque` for high-performance enqueue and dequeue operations.
3.  **Triage Fairness:** Strictly follows the First-In-First-Out principle to ensure patients are seen in their arrival order.
4.  **Audit Trail Capability:** Captures patient metadata and arrival timestamps for performance monitoring and clinical reporting.

### Complexity Analysis
- **Issue Token (Enqueue):** $O(1)$
- **Call Next (Dequeue):** $O(1)$
- **Peek Next:** $O(1)$
- **Space:** $O(N)$
