import heapq
from typing import Dict, List, Tuple, Optional

class RailwayMap:
    """
    Railway Map Navigator using Dijkstra's Algorithm.
    """

    def __init__(self):
        self._adj: Dict[str, List[Tuple[str, float]]] = {}

    def add_connection(self, u: str, v: str, weight: float) -> None:
        """Adds a bi-directional railway track."""
        if u not in self._adj: self._adj[u] = []
        if v not in self._adj: self._adj[v] = []
        self._adj[u].append((v, weight))
        self._adj[v].append((u, weight))

    def find_shortest_route(self, start: str, end: str) -> Tuple[Optional[List[str]], float]:
        """
        Finds the shortest path between two stations.
        Time Complexity: O((V+E) log V)
        """
        if start not in self._adj or end not in self._adj:
            return None, float('inf')

        pq = [(0.0, start, [start])]
        visited = {}

        while pq:
            cost, current, path = heapq.heappop(pq)

            if current == end:
                return path, cost

            if current in visited and visited[current] <= cost:
                continue
            visited[current] = cost

            for neighbor, weight in self._adj.get(current, []):
                new_cost = cost + weight
                if neighbor not in visited or new_cost < visited[neighbor]:
                    heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

        return None, float('inf')
