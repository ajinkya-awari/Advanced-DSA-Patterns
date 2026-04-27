from typing import List

class WeatherTree:
    """Range Minimum Query (RMQ) using Segment Tree."""
    def __init__(self, temperatures: List[float]):
        self._n = len(temperatures)
        self._tree = [0.0] * (4 * self._n)
        if temperatures:
            self._build(temperatures, 1, 0, self._n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self._tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        self._tree[node] = max(self._tree[2 * node], self._tree[2 * node + 1])

    def query_max(self, l: int, r: int) -> float:
        return self._query(1, 0, self._n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l: return -float('inf')
        if l <= start and end <= r: return self._tree[node]
        mid = (start + end) // 2
        return max(self._query(2 * node, start, mid, l, r),
                   self._query(2 * node + 1, mid + 1, end, l, r))
