import pytest
from hospital_management_system import HospitalSystem

def test_hospital_triage():
    hs = HospitalSystem()
    hs.triage_patient("John", 5) # Mid
    hs.triage_patient("Alice", 10) # Critical
    hs.triage_patient("Bob", 1) # Stable
    
    assert hs.treat_next() == "Alice"
    assert hs.treat_next() == "John"
    assert hs.treat_next() == "Bob"
