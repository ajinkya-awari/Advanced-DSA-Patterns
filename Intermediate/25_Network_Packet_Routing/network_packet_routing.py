import heapq
from typing import List, Dict, Tuple, Optional, Set, Final
from dataclasses import dataclass, field

@dataclass(frozen=True)
class RouteResult:
    """Metadata regarding a completed packet route."""
    path: List[str]
    total_latency: float
    hops: int

class NetworkRouter:
    """
    Enterprise-grade Network Packet Routing Engine using Dijkstra's Algorithm.
    """

    def __init__(self):
        # Adjacency list: router_id -> list of (neighbor_id, weight)
        self._topology: Dict[str, List[Tuple[str, float]]] = {}

    def add_link(self, router_a: str, router_b: str, latency: float) -> None:
        """
        Adds a directed link between two routers.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if latency < 0:
            raise ValueError("Latency cannot be negative.")
        
        if router_a not in self._topology:
            self._topology[router_a] = []
        if router_b not in self._topology:
            self._topology[router_b] = []
            
        self._topology[router_a].append((router_b, latency))

    def find_route(self, source: str, destination: str) -> Optional[RouteResult]:
        """
        Calculates the optimal route using Dijkstra's algorithm.
        
        Time Complexity: O((V + E) log V)
        Space Complexity: O(V)
        """
        if source not in self._topology or destination not in self._topology:
            return None

        # Min-heap stores: (cumulative_latency, current_router)
        priority_queue: List[Tuple[float, str]] = [(0.0, source)]
        
        # Latency tracking: router -> min_latency found so far
        min_latencies: Dict[str, float] = {source: 0.0}
        
        # Path reconstruction: current -> predecessor
        predecessors: Dict[str, Optional[str]] = {source: None}

        while priority_queue:
            current_latency, current_router = heapq.heappop(priority_queue)

            # Optimization: Skip if we found a better path already
            if current_latency > min_latencies.get(current_router, float('inf')):
                continue

            if current_router == destination:
                return self._reconstruct_route(predecessors, destination, current_latency)

            for neighbor, weight in self._topology.get(current_router, []):
                latency = current_latency + weight
                
                if latency < min_latencies.get(neighbor, float('inf')):
                    min_latencies[neighbor] = latency
                    predecessors[neighbor] = current_router
                    heapq.heappush(priority_queue, (latency, neighbor))

        # Check for source == destination specifically if loop finished
        if source == destination:
             return self._reconstruct_route(predecessors, destination, 0.0)

        return None

    def _reconstruct_route(self, predecessors: Dict[str, Optional[str]], 
                          destination: str, total_latency: float) -> RouteResult:
        """Backtracks from destination to build the path list."""
        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = predecessors.get(current)
        
        full_path = path[::-1]
        return RouteResult(
            path=full_path,
            total_latency=total_latency,
            hops=len(full_path) - 1
        )

    @property
    def router_count(self) -> int:
        return len(self._topology)
