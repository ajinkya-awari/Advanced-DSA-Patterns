import heapq
from typing import Dict, List, Tuple, Optional

class TrafficRouter:
    """
    Advanced Router using Dijkstra with dynamic traffic density weights.
    """

    def __init__(self):
        self._adj: Dict[str, List[Tuple[str, float]]] = {}

    def add_road(self, u: str, v: str, distance: float) -> None:
        if u not in self._adj: self._adj[u] = []
        self._adj[u].append((v, distance))

    def find_fastest_path(self, start: str, end: str, traffic_factors: Dict[Tuple[str, str], float]) -> Tuple[Optional[List[str]], float]:
        """
        Calculates path where weight = distance * traffic_factor.
        """
        pq = [(0.0, start, [start])]
        visited = {}

        while pq:
            time, current, path = heapq.heappop(pq)

            if current == end:
                return path, time

            if current in visited and visited[current] <= time:
                continue
            visited[current] = time

            for neighbor, distance in self._adj.get(current, []):
                # Apply traffic factor (default 1.0 if not specified)
                factor = traffic_factors.get((current, neighbor), 1.0)
                travel_time = distance * factor
                
                new_time = time + travel_time
                if neighbor not in visited or new_time < visited[neighbor]:
                    heapq.heappush(pq, (new_time, neighbor, path + [neighbor]))

        return None, float('inf')
