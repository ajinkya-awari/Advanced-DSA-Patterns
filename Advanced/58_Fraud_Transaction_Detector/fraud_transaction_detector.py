from typing import Dict, List, Set

class FraudDetector:
    """Fraud detection using Graph cycle identification."""
    def __init__(self):
        self._adj: Dict[str, List[str]] = {}

    def add_transaction(self, u: str, v: str):
        if u not in self._adj: self._adj[u] = []
        self._adj[u].append(v)

    def has_cycle(self) -> bool:
        visited = set()
        stack = set()
        for node in list(self._adj.keys()):
            if node not in visited:
                if self._dfs(node, visited, stack): return True
        return False

    def _dfs(self, node: str, visited: Set[str], stack: Set[str]) -> bool:
        visited.add(node)
        stack.add(node)
        for neighbor in self._adj.get(node, []):
            if neighbor not in visited:
                if self._dfs(neighbor, visited, stack): return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False
