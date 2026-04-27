from typing import List, Tuple

class DisjointSet:
    def __init__(self, nodes: List[str]):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, i: str) -> str:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]

    def union(self, i: str, j: str) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

class ElectricityGridOptimizer:
    """
    Optimizes grid wiring costs using Kruskal's MST algorithm.
    """

    def __init__(self, stations: List[str]):
        self._stations = stations
        self._edges: List[Tuple[float, str, str]] = []

    def add_cable_option(self, u: str, v: str, cost: float) -> None:
        self._edges.append((cost, u, v))

    def get_optimal_grid(self) -> Tuple[List[Tuple[str, str]], float]:
        """
        Finds the Minimum Spanning Tree for the grid.
        Time Complexity: O(E log E)
        """
        self._edges.sort() # Sort by cost
        dsu = DisjointSet(self._stations)
        mst = []
        total_cost = 0.0

        for cost, u, v in self._edges:
            if dsu.union(u, v):
                mst.append((u, v))
                total_cost += cost
        
        return mst, total_cost
