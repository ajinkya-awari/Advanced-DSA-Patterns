# Advanced DSA & System Design Architecture (60+ Patterns)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

A production-grade algorithmic portfolio demonstrating 60 enterprise-level implementation patterns. This repository showcases optimized data structures, complex algorithm design, and rigorous system engineering standards expected at FAANG companies.

## 🚀 Engineering Standards

Every project in this repository adheres to strict industry-level software engineering principles:

*   **Paradigms:** Pure Object-Oriented (OOP) and Functional programming.
*   **Complexity:** Every module includes documented Time ($O(N)$) and Space complexity.
*   **Testing:** 100% coverage using `pytest` (Happy Path, Null Path, Bounds, and Edge Cases).
*   **Robustness:** Integrated validation for type safety, memory bounds, and extreme values.
*   **Clean Code:** Semantic, domain-specific naming conventions—zero "robotic" or generic identifiers.

---

## 🏗️ Portfolio Architecture

The portfolio is structured into three phases of increasing complexity, reflecting a progression from foundational structures to complex system simulations.

### Phase 1: Beginner (Foundational Data Structures)
*Focus: Linear memory management, pointer manipulation, and LIFO/FIFO protocols.*

1.  **Student Record System:** Contiguous array storage with index-shifting optimization.
2.  **Contact Book:** Singly Linked List with dynamic memory allocation.
3.  **Undo/Redo Feature:** Dual-stack architecture for atomic state transitions.
4.  **Printer Queue:** FIFO management using double-ended queues.
5.  **Browser History:** Doubly Linked List for bidirectional navigation.
6.  **Music Playlist:** Singly Circular Linked List for continuous loop logic.
7.  **Balanced Brackets:** Stack-based syntax validation for compiler front-ends.
8.  **Railway Reservation:** Hybrid List/Queue system with waitlist promotion.
9.  **Hospital Token System:** Deterministic token generation and FIFO triage.
10. **Palindrome Checker:** Bidirectional deque validation with $O(N)$ efficiency.
11. **Spell Checker:** Custom Hash Table with Chaining and Dynamic Rehashing.
12. **Leaderboard Ranking:** Binary-search insertion for top-K optimization.
13. **Library Management:** Stateful tracking with ISBN-based unique indexing.
14. **Parking Lot Manager:** LIFO corridor simulation with obstruction handling.
15. **Online Exam System:** State-machine based progression and scoring.
16. **File Compression:** Huffman Coding simulation via greedy tree construction.
17. **Simple Text Editor:** Stack-based command pattern for document history.
18. **Maze Solver:** Breadth-First Search (BFS) for shortest path guarantee.
19. **Phone Directory:** Hash Map retrieval with case-insensitive normalization.
20. **Bank Account System:** Linked List ledger with $O(1)$ tail-pointer tracking.

### Phase 2: Intermediate (Non-Linear Structures & Graph Theory)
*Focus: Hierarchical data, search optimization, and shortest-path algorithms.*

21. **Autocomplete Engine:** Trie (Prefix Tree) for $O(L)$ word discovery.
22. **Dictionary App:** Hybrid Trie-HashMap for $O(1)$ lookup and prefix discovery.
23. **Chat Application:** Message Broker pattern with global and local queues.
24. **Pathfinding Visualizer:** Comparative benchmarking of BFS and DFS algorithms.
25. **Network Packet Routing:** Dijkstra's Algorithm for optimal throughput in graphs.
26. **Job Scheduler:** Max-Priority Queue (Heap) with lazy deletion support.
27. **Movie Recommendation:** Bipartite Graph Collaborative Filtering.
28. **Family Tree Generator:** Binary Tree with recursive lineage traversal.
29. **Expression Evaluator:** Shunting-yard algorithm for infix-to-postfix conversion.
30. **Turn Manager:** Circular Queue for dynamic multiplayer turn rotation.
31. **LRU Cache:** Doubly Linked List + HashMap for $O(1)$ eviction.
32. **Task Scheduler:** Heap + Queue management with task cooldowns.
33. **Railway Map Navigator:** Dijkstra's implementation for station-to-station routing.
34. **AI Snake Game:** Deque-based segments and BFS pathfinding to food.
35. **Elevator Simulation:** SCAN scheduling algorithm for directional optimization.
36. **Social Media Suggestions:** Graph traversal for second-degree mutual friends.
37. **Online Judge Leaderboard:** Real-time Max-Heap updates for global rankings.
38. **Chatbot Suggestion:** Intent-prefix mapping using Trie + HashMap.
39. **Online Auction System:** Concurrent bid tracking via distributed Heaps.
40. **File System Simulation:** Tree-based directory hierarchy with content hashing.

### Phase 3: Advanced (Optimization & System Simulation)
*Focus: Dynamic Programming, Cryptography, and Complex Algorithmic Systems.*

41. **Plagiarism Checker:** Rabin-Karp Rolling Hash for multi-document overlap.
42. **Search Engine:** Trie-based indexing with term frequency (TF) ranking.
43. **Blockchain Simulation:** Hash-Linked List with integrity validation.
44. **Version Control System:** Commit DAG (Directed Acyclic Graph) for branching.
45. **Traffic Navigation:** Dijkstra with dynamic edge weights based on traffic.
46. **Electricity Grid:** Kruskal’s Minimum Spanning Tree for wiring optimization.
47. **Airline Flight Scheduler:** Weighted Directed Graph for multi-hop connections.
48. **DNA Sequence Analyzer:** Dynamic Programming for Longest Common Subsequence.
49. **Spam Email Filter:** Hash-based pattern matching for intent recognition.
50. **Matchmaking System:** Disjoint Set Union (DSU) for skill-based clustering.
51. **Memory Allocator:** Min-Heap based "Best Fit" allocation simulator.
52. **Distributed File Sharing:** Graph + DSU for peer-to-peer connectivity.
53. **AI Chess Game:** Minimax algorithm with Alpha-Beta Pruning.
54. **Hospital ER Triage:** Priority-based scheduling for critical care.
55. **Weather Data Manager:** Segment Tree for high-speed range queries.
56. **Log Analyzer:** High-volume pattern parsing via Trie + HashMap.
57. **Auto-Correct Keyboard:** Trie + Levenshtein Distance for typo correction.
58. **Fraud Detector:** Cycle detection in graphs for transaction rings.
59. **Image Compression Tool:** Pixel-weighted Huffman encoding simulation.
60. **Compiler Design:** Abstract Syntax Tree (AST) construction for expressions.

---

## 🛠️ Setup and Verification

### Prerequisites
- Python 3.10 or higher
- `pytest` for unit test execution

### Installation
```bash
git clone https://github.com/ajinkya-awari/Advanced-DSA-Patterns.git
cd Advanced-DSA-Patterns
pip install pytest
```

### Running Tests
To verify the entire portfolio (60 projects):
```bash
pytest .
```

To test a specific phase:
```bash
pytest Beginner/
```

---

## 👤 Author
**Ajinkya Awari**
- Computer Science Master's Graduate
- 3 Years Industry Experience in Software Engineering
- Specialized in Distributed Systems & Algorithmic Optimization

---
*This repository is built as a technical showcase for Senior SDE / SDE II roles.*
