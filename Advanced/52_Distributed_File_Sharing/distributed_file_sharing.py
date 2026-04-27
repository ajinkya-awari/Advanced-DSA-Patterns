from typing import Dict, List, Set

class P2PNetwork:
    """Distributed File Sharing connectivity using DSU."""
    def __init__(self, nodes: List[str]):
        self.parent = {n: n for n in nodes}
        self._files: Dict[str, Set[str]] = {n: set() for n in nodes}

    def find(self, i: str) -> str:
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def connect(self, u: str, v: str):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v: self.parent[root_u] = root_v

    def share_file(self, node: str, filename: str):
        self._files[node].add(filename)

    def get_accessible_files(self, node: str) -> Set[str]:
        root = self.find(node)
        all_files = set()
        for n in self.parent:
            if self.find(n) == root:
                all_files.update(self._files[n])
        return all_files
