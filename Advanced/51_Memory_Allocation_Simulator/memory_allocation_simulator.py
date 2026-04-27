import heapq
from typing import List, Tuple, Optional

class MemorySimulator:
    """OS-level memory allocator using Min-Heap for Best Fit."""
    def __init__(self, total_size: int):
        # (size, start_offset)
        self._free_blocks: List[Tuple[int, int]] = [(total_size, 0)]
        self._allocated: Dict[int, int] = {} # offset -> size

    def malloc(self, size: int) -> Optional[int]:
        """Time: O(N) for search in this simplified simulation."""
        self._free_blocks.sort() # Ensure we pick the smallest sufficient block (Best Fit)
        for i, (b_size, offset) in enumerate(self._free_blocks):
            if b_size >= size:
                self._free_blocks.pop(i)
                if b_size > size:
                    self._free_blocks.append((b_size - size, offset + size))
                self._allocated[offset] = size
                return offset
        return None

    def free(self, offset: int):
        if offset in self._allocated:
            size = self._allocated.pop(offset)
            self._free_blocks.append((size, offset))
            # In a real OS, we would coalesce adjacent free blocks here.
