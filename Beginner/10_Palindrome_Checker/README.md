# Palindrome Checker (Deque)

### Architectural Overview
The **Palindrome Checker** utilizes a **Double-Ended Queue (Deque)** to validate string symmetry.

**Core Design Decisions:**
1.  **Bidirectional Comparison:** Pops elements from both ends of the deque in $O(1)$ time, verifying that the characters match at every step until the center is reached.
2.  **Robust Sanitization:** Uses regular expressions to strip non-alphanumeric characters and normalizes casing to provide consistent results regardless of punctuation.
3.  **Linear Efficiency:** The single-pass scan and subsequent bidirectional reduction ensure $O(N)$ time complexity.

### Complexity Analysis
- **Validation:** $O(N)$
- **Space:** $O(N)$ (to store sanitized string in deque)
