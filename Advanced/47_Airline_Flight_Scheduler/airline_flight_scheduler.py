import heapq
from typing import Dict, List, Tuple, Optional

class FlightScheduler:
    """Advanced Airline Flight Scheduler using Dijkstra's."""
    def __init__(self):
        self._adj: Dict[str, List[Tuple[str, float]]] = {}

    def add_flight(self, origin: str, dest: str, duration: float):
        if origin not in self._adj: self._adj[origin] = []
        self._adj[origin].append((dest, duration))

    def find_optimal_route(self, start: str, end: str) -> Tuple[Optional[List[str]], float]:
        pq = [(0.0, start, [start])]
        visited = {}
        while pq:
            time, current, path = heapq.heappop(pq)
            if current == end: return path, time
            if current in visited and visited[current] <= time: continue
            visited[current] = time
            for neighbor, duration in self._adj.get(current, []):
                new_time = time + duration
                if neighbor not in visited or new_time < visited[neighbor]:
                    heapq.heappush(pq, (new_time, neighbor, path + [neighbor]))
        return None, float('inf')
