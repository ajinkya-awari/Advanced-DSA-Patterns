from typing import List, Optional
from collections import deque
from dataclasses import dataclass

@dataclass
class PrintJob:
    """Represents a print job entity."""
    job_id: int
    document_name: str
    pages: int

class PrinterQueue:
    """
    Production-grade Printer Queue Manager using FIFO logic.
    
    Attributes:
        _queue (deque): The underlying double-ended queue for jobs.
        _completed_jobs (List[PrintJob]): History of processed jobs.
    """

    def __init__(self):
        self._queue: deque[PrintJob] = deque()
        self._completed_jobs: List[PrintJob] = []

    def add_job(self, job_id: int, document_name: str, pages: int) -> None:
        """
        Adds a new print job to the end of the queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if pages <= 0:
            raise ValueError("Page count must be greater than zero.")
        
        new_job = PrintJob(job_id, document_name, pages)
        self._queue.append(new_job)

    def process_next_job(self) -> Optional[PrintJob]:
        """
        Processes and removes the job at the front of the queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._queue:
            raise IndexError("Cannot process job: Printer queue is empty.")
        
        current_job = self._queue.popleft()
        self._completed_jobs.append(current_job)
        return current_job

    def cancel_job(self, job_id: int) -> bool:
        """
        Removes a specific job from the queue by ID.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        for job in self._queue:
            if job.job_id == job_id:
                self._queue.remove(job)
                return True
        return False

    @property
    def pending_count(self) -> int:
        return len(self._queue)

    @property
    def history_count(self) -> int:
        return len(self._completed_jobs)

    def get_queue_snapshot(self) -> List[PrintJob]:
        """Returns a list of all pending jobs."""
        return list(self._queue)
