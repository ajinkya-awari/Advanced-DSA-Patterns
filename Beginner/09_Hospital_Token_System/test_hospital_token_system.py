import pytest
from hospital_token_system import HospitalTokenSystem

@pytest.fixture
def hospital():
    return HospitalTokenSystem()

def test_token_issuance(hospital):
    """Verify that tokens are issued sequentially."""
    t1 = hospital.issue_token("Alice")
    t2 = hospital.issue_token("Bob")
    
    assert t1.token_number == 1
    assert t2.token_number == 2
    assert hospital.get_waiting_count() == 2

def test_fifo_behavior(hospital):
    """Verify patients are called in the order they arrived."""
    hospital.issue_token("Alice")
    hospital.issue_token("Bob")
    
    next_p = hospital.call_next_patient()
    assert next_p.patient_name == "Alice"
    assert hospital.get_waiting_count() == 1

def test_empty_queue_exception(hospital):
    """Verify system raises error when calling from empty queue."""
    with pytest.raises(IndexError, match="No patients in the waiting queue"):
        hospital.call_next_patient()

def test_invalid_patient_name(hospital):
    """Verify validation for empty names."""
    with pytest.raises(ValueError, match="cannot be empty"):
        hospital.issue_token("   ")

def test_peek_next(hospital):
    """Verify next patient can be viewed without removal."""
    hospital.issue_token("Charlie")
    next_p = hospital.peek_next_patient()
    assert next_p.patient_name == "Charlie"
    assert hospital.get_waiting_count() == 1

def test_sequential_consistency(hospital):
    """Verify token counter persists across calls."""
    hospital.issue_token("A")
    hospital.call_next_patient()
    t2 = hospital.issue_token("B")
    assert t2.token_number == 2
