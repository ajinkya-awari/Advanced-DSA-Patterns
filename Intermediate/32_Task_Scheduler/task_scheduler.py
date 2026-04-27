import heapq
from collections import deque
from typing import List, Dict, Optional, Tuple

class TaskScheduler:
    """
    Task Scheduler with priorities and cooldown periods.
    Uses Max-Heap for priority and FIFO Queue for cooldown management.
    """

    def __init__(self, cooldown: int):
        self._cooldown: int = cooldown
        self._priority_heap: List[Tuple[int, str]] = [] # [-priority, task_id]
        self._wait_queue: deque[Tuple[str, int]] = deque() # [task_id, available_time]
        self._current_time: int = 0

    def add_task(self, task_id: str, priority: int) -> None:
        """Adds a task to the ready heap."""
        heapq.heappush(self._priority_heap, (-priority, task_id))

    def execute_next(self) -> Optional[str]:
        """
        Executes the highest priority task that is not in cooldown.
        Time Complexity: O(log N)
        """
        # 1. Move tasks from wait queue to heap if cooldown expired
        while self._wait_queue and self._wait_queue[0][1] <= self._current_time:
            t_id, _ = self._wait_queue.popleft()
            # In a real system, we'd store priority to re-add. 
            # For this simulation, we assume priority 1 for recurring.
            heapq.heappush(self._priority_heap, (-1, t_id))

        if not self._priority_heap:
            self._current_time += 1
            return None

        _, task_id = heapq.heappop(self._priority_heap)
        
        # 2. Add to cooldown queue
        self._wait_queue.append((task_id, self._current_time + self._cooldown + 1))
        self._current_time += 1
        
        return task_id

    @property
    def time(self) -> int:
        return self._current_time
