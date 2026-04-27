# Movie Recommendation System (Graph + HashMap)

### Architectural Overview
The **Movie Recommendation System** utilizes a **Bipartite Graph** representing interactions between Users and Movies, leveraging User-User Collaborative Filtering to generate content suggestions.

**Core Design Decisions:**
1.  **Dual Adjacency Mapping:** Maintains bi-directional links (User -> Movies and Movie -> Users) to enable efficient graph traversal from a target user to their peer group.
2.  **Unique Peer Discovery:** Isolates unique users who share at least one interest with the target, preventing contributions from being over-weighted by users with multiple shared likes.
3.  **Collaborative Interest Discovery:** Analyzes the aggregate preferences of the peer group to identify movies that are popular within the target user's specific social neighborhood.
4.  **$O(1)$ Metadata Registry:** Uses HashMaps to store movie details, ensuring that metadata resolution remains a constant-time operation.

### Complexity Analysis
- **Generate Recommendations:** $O(U \times M)$ where $U$ is similar users and $M$ is their combined movie preference sets.
- **Add Preference:** $O(1)$.
- **Space:** $O(User \times AvgLikes)$ for graph connectivity.
