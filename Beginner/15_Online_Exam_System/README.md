# Online Exam System (Array)

### Architectural Overview
The **Online Exam System** is implemented using a **Contiguous Array** of `Question` entities to model a linear examination workflow.

**Core Design Decisions:**
1.  **Indexed Navigation:** Leverages $O(1)$ array access to allow candidates to move between questions seamlessly.
2.  **Submission Lock:** Implements a state-locked response mechanism to prevent post-submission tampering.
3.  **Encapsulated Scoring Engine:** Performs a single-pass $O(N)$ comparison between responses and ground truth to generate objective results.
4.  **Immutability Invariant:** Question entities are frozen after creation to ensure audit trail consistency.

### Complexity Analysis
- **Navigation (Next/Prev):** $O(1)$
- **Record Answer:** $O(1)$
- **Score Calculation:** $O(N)$
- **Space:** $O(N)$
