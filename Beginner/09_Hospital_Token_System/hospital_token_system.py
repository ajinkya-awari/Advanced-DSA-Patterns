from typing import List, Optional, Final
from collections import deque
from dataclasses import dataclass
from datetime import datetime

@dataclass
class PatientToken:
    """Represents a patient's position and metadata in the queue."""
    token_number: int
    patient_name: str
    arrival_time: datetime

class HospitalTokenSystem:
    """
    Enterprise-grade Hospital Token Management System using FIFO Queue.
    
    Attributes:
        _queue (deque[PatientToken]): The underlying FIFO queue.
        _token_counter (int): Sequential counter for token generation.
    """

    def __init__(self):
        self._queue: deque[PatientToken] = deque()
        self._token_counter: int = 1

    def issue_token(self, patient_name: str) -> PatientToken:
        """
        Generates and enqueues a new token for a patient.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not patient_name.strip():
            raise ValueError("Patient name cannot be empty.")

        new_token = PatientToken(
            token_number=self._token_counter,
            patient_name=patient_name,
            arrival_time=datetime.now()
        )
        
        self._queue.append(new_token)
        self._token_counter += 1
        return new_token

    def call_next_patient(self) -> PatientToken:
        """
        Retrieves and removes the next patient from the queue for consultation.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._queue:
            raise IndexError("Consultation error: No patients in the waiting queue.")
            
        return self._queue.popleft()

    def get_waiting_count(self) -> int:
        """Returns the total number of patients currently waiting."""
        return len(self._queue)

    def peek_next_patient(self) -> Optional[PatientToken]:
        """Returns the next patient in line without removing them."""
        return self._queue[0] if self._queue else None

    def get_all_pending_tokens(self) -> List[PatientToken]:
        """Returns a snapshot of all currently waiting patients."""
        return list(self._queue)
