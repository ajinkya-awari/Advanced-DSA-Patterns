from typing import Dict, List

class Matchmaker:
    """Multiplayer Matchmaking using Disjoint Set Union."""
    def __init__(self, players: List[str]):
        self.parent = {p: p for p in players}
        self.rank = {p: 0 for p in players}

    def find(self, i: str) -> str:
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: str, j: str):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]: self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]: self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
