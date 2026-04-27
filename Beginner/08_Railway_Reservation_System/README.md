# Railway Reservation System (Queue)

### Architectural Overview
The **Railway Reservation System** manages a finite pool of confirmed seats and an overflow FIFO queue for the waitlist.

**Core Design Decisions:**
1.  **State Promotion Logic:** When a confirmed seat is vacated, the system promotes the first passenger from the waitlist in $O(1)$ time, ensuring optimal coach occupancy.
2.  **Waitlist Management:** Utilizes a `collections.deque` for the waitlist to guarantee First-In-First-Out fairness for all ticket requests.
3.  **Encapsulated Logic:** Status transition logic is internal to the system, providing a clean API for booking and cancellation while maintaining data integrity.

### Complexity Analysis
- **Booking:** $O(1)$
- **Cancellation:** $O(N)$ (requires searching lists/deques)
- **Promotion:** $O(1)$
- **Space:** $O(N)$
