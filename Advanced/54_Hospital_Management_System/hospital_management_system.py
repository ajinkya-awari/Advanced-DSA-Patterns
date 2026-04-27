import heapq
from dataclasses import dataclass, field
from typing import Optional

@dataclass(order=True)
class Patient:
    priority: int # Higher = more urgent
    name: str = field(compare=False)

class HospitalSystem:
    """Emergency Room triage using Max-Heap."""
    def __init__(self):
        self._heap = []

    def triage_patient(self, name: str, severity: int):
        # Python heapq is min-heap, so we negate priority
        heapq.heappush(self._heap, (-severity, name))

    def treat_next(self) -> Optional[str]:
        if not self._heap: return None
        _, name = heapq.heappop(self._heap)
        return name
