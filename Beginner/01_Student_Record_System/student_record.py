from typing import List, Optional, Final
from dataclasses import dataclass

@dataclass
class Student:
    """Represents a Student entity in the system."""
    student_id: int
    full_name: str
    gpa: float

class StudentRecordSystem:
    """
    An enterprise-grade Student Record System using contiguous array structures.
    
    Attributes:
        capacity (int): The maximum number of records the system can hold.
        records (List[Optional[Student]]): The underlying array structure.
        size (int): Current number of active records.
    """

    def __init__(self, capacity: int = 100):
        self._capacity: Final[int] = capacity
        self._records: List[Optional[Student]] = [None] * capacity
        self._size: int = 0

    def _find_index(self, student_id: int) -> int:
        """
        Locates the array index of a student by ID.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        for i in range(self._size):
            if self._records[i] and self._records[i].student_id == student_id:
                return i
        return -1

    def create_student(self, student_id: int, name: str, gpa: float) -> bool:
        """
        Adds a new student to the array.
        
        Time Complexity: O(N) due to duplicate check.
        Space Complexity: O(1)
        """
        if self._size >= self._capacity:
            raise MemoryError("System capacity reached. Cannot add more records.")

        if self._find_index(student_id) != -1:
            raise ValueError(f"Student with ID {student_id} already exists.")

        new_student = Student(student_id, name, gpa)
        self._records[self._size] = new_student
        self._size += 1
        return True

    def read_student(self, student_id: int) -> Student:
        """
        Retrieves a student record by ID.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        index = self._find_index(student_id)
        if index == -1:
            raise KeyError(f"Student ID {student_id} not found.")
        return self._records[index]

    def update_student(self, student_id: int, name: Optional[str] = None, gpa: Optional[float] = None) -> bool:
        """
        Updates an existing student's information.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        index = self._find_index(student_id)
        if index == -1:
            raise KeyError(f"Student ID {student_id} not found.")

        student = self._records[index]
        if name:
            student.full_name = name
        if gpa is not None:
            student.gpa = gpa
        return True

    def delete_student(self, student_id: int) -> bool:
        """
        Deletes a student and shifts trailing elements to maintain contiguity.
        
        Time Complexity: O(N) due to array shifting.
        Space Complexity: O(1)
        """
        index = self._find_index(student_id)
        if index == -1:
            raise KeyError(f"Student ID {student_id} not found.")

        # Shift elements to the left to fill the gap
        for i in range(index, self._size - 1):
            self._records[i] = self._records[i + 1]

        self._records[self._size - 1] = None
        self._size -= 1
        return True

    def get_all_records(self) -> List[Student]:
        """Returns all active student records."""
        return [self._records[i] for i in range(self._size)]

    @property
    def current_size(self) -> int:
        return self._size
