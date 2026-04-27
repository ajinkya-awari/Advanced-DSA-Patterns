import pytest
from online_exam_system import OnlineExam, Question

@pytest.fixture
def sample_exam():
    qs = [
        Question(1, "What is 2+2?", ["3", "4", "5"], 1),
        Question(2, "What is the capital of France?", ["London", "Paris", "Berlin"], 1),
        Question(3, "Which DS uses LIFO?", ["Stack", "Queue", "Array"], 0)
    ]
    return OnlineExam(qs)

def test_exam_navigation(sample_exam):
    """Verify O(1) index-based navigation."""
    assert sample_exam.get_current_question().question_id == 1
    assert sample_exam.next_question() is True
    assert sample_exam.get_current_question().question_id == 2
    assert sample_exam.previous_question() is True
    assert sample_exam.get_current_question().question_id == 1

def test_record_and_calculate_score(sample_exam):
    """Verify score calculation logic."""
    # Correct answer for Q1
    sample_exam.record_answer(1) 
    sample_exam.next_question()
    # Correct answer for Q2
    sample_exam.record_answer(1)
    sample_exam.next_question()
    # Wrong answer for Q3
    sample_exam.record_answer(1)
    
    score = sample_exam.submit_exam()
    assert score == 2
    assert sample_exam.is_submitted is True

def test_submission_lock(sample_exam):
    """Verify answers cannot be changed after submission."""
    sample_exam.submit_exam()
    with pytest.raises(RuntimeError, match="after submission"):
        sample_exam.record_answer(0)

def test_invalid_option_index(sample_exam):
    """Verify bounds checking for option selection."""
    with pytest.raises(ValueError, match="Invalid option index"):
        sample_exam.record_answer(10)

def test_empty_exam_prevention():
    """Verify that exams must have content."""
    with pytest.raises(ValueError, match="at least one question"):
        OnlineExam([])

def test_progress_tracking(sample_exam):
    """Verify progress percentage calculation."""
    assert sample_exam.progress == 0
    sample_exam.record_answer(1)
    assert sample_exam.progress == (1/3) * 100
