import heapq
from typing import List, Dict, Optional, Final, Any
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Job:
    """Immutable representation of a scheduled task."""
    job_id: str
    priority: int  # Higher value = Higher priority
    task_name: str
    payload: Any = None

class JobScheduler:
    """
    Enterprise-grade Job Scheduler using a Max-Priority Queue with lazy removal.
    """

    def __init__(self):
        self._heap: List[List[Any]] = []  # Elements: [-priority, sequence, job_id]
        self._entry_finder: Dict[str, Job] = {}
        self._removed_ids: set[str] = set()
        self._counter: int = 0  # For FIFO tie-breaking

    def schedule_job(self, job_id: str, priority: int, task_name: str, payload: Any = None) -> None:
        """
        Adds a new job to the scheduler.
        
        Time Complexity: O(log N)
        Space Complexity: O(1) for insertion.
        """
        if job_id in self._entry_finder:
            raise ValueError(f"Job ID {job_id} is already in the queue.")

        job = Job(job_id, priority, task_name, payload)
        self._entry_finder[job_id] = job
        
        # Negate priority for Max-Heap behavior
        entry = [-priority, self._counter, job_id]
        self._counter += 1
        heapq.heappush(self._heap, entry)

    def cancel_job(self, job_id: str) -> bool:
        """
        Marks a job for removal (Lazy Deletion).
        
        Time Complexity: O(1) average.
        """
        if job_id in self._entry_finder:
            self._removed_ids.add(job_id)
            del self._entry_finder[job_id]
            return True
        return False

    def get_next_job(self) -> Optional[Job]:
        """
        Retrieves and removes the highest priority job.
        
        Time Complexity: Amortized O(log N)
        """
        while self._heap:
            priority_neg, seq, job_id = heapq.heappop(self._heap)
            if job_id not in self._removed_ids:
                if job_id in self._entry_finder:
                    job = self._entry_finder.pop(job_id)
                    return job
            else:
                self._removed_ids.remove(job_id)
        
        return None

    def peek_next_job(self) -> Optional[Job]:
        """Returns the highest priority job without removing it."""
        while self._heap:
            priority_neg, seq, job_id = self._heap[0]
            if job_id in self._removed_ids:
                heapq.heappop(self._heap)
                self._removed_ids.remove(job_id)
            else:
                return self._entry_finder[job_id]
        return None

    @property
    def pending_count(self) -> int:
        return len(self._entry_finder)
