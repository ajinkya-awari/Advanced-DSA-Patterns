from typing import List, Dict, Optional, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class Question:
    """Immutable entity representing an exam question."""
    question_id: int
    text: str
    options: List[str]
    correct_option_index: int

class OnlineExam:
    """
    Enterprise-grade Exam System using indexed array structures.
    
    Attributes:
        _questions (List[Question]): Internal array of questions.
        _responses (Dict[int, int]): Mapping of question_id to candidate's answer index.
        _current_idx (int): Tracker for exam progression.
    """

    def __init__(self, questions: List[Question]):
        if not questions:
            raise ValueError("Exam must contain at least one question.")
        self._questions: Final[List[Question]] = questions
        self._responses: Dict[int, int] = {}
        self._current_idx: int = 0
        self._is_submitted: bool = False

    def get_current_question(self) -> Question:
        """Retrieves the question at the current index."""
        return self._questions[self._current_idx]

    def next_question(self) -> bool:
        """Advances to the next question. Returns False if at end."""
        if self._current_idx < len(self._questions) - 1:
            self._current_idx += 1
            return True
        return False

    def previous_question(self) -> bool:
        """Moves to the previous question."""
        if self._current_idx > 0:
            self._current_idx -= 1
            return True
        return False

    def record_answer(self, option_index: int) -> None:
        """Records the candidate's response for the current question."""
        if self._is_submitted:
            raise RuntimeError("Cannot modify answers after submission.")
        
        current_q = self.get_current_question()
        if not (0 <= option_index < len(current_q.options)):
            raise ValueError("Invalid option index.")
            
        self._responses[current_q.question_id] = option_index

    def submit_exam(self) -> int:
        """
        Calculates and returns the final score.
        Time Complexity: O(N) where N is number of questions.
        """
        if self._is_submitted:
            return self._calculate_score()
            
        self._is_submitted = True
        return self._calculate_score()

    def _calculate_score(self) -> int:
        score = 0
        for q in self._questions:
            if self._responses.get(q.question_id) == q.correct_option_index:
                score += 1
        return score

    @property
    def progress(self) -> float:
        """Returns percentage of questions answered."""
        return (len(self._responses) / len(self._questions)) * 100

    @property
    def is_submitted(self) -> bool:
        return self._is_submitted
