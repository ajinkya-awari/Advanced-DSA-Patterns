import pytest
from student_record import StudentRecordSystem

@pytest.fixture
def system():
    return StudentRecordSystem(capacity=5)

def test_create_read_happy_path(system):
    """Verify successful creation and retrieval of records."""
    system.create_student(101, "John Doe", 3.8)
    student = system.read_student(101)
    assert student.full_name == "John Doe"
    assert system.current_size == 1

def test_duplicate_id_insertion(system):
    """Ensure system prevents duplicate primary keys."""
    system.create_student(101, "John Doe", 3.8)
    with pytest.raises(ValueError, match="already exists"):
        system.create_student(101, "Jane Smith", 3.9)

def test_update_record(system):
    """Verify field updates."""
    system.create_student(101, "John Doe", 3.8)
    system.update_student(101, name="John Updated", gpa=4.0)
    student = system.read_student(101)
    assert student.full_name == "John Updated"
    assert student.gpa == 4.0

def test_delete_and_shift(system):
    """Verify deletion and that array shifts correctly to maintain order."""
    system.create_student(101, "User A", 3.0)
    system.create_student(102, "User B", 3.5)
    system.create_student(103, "User C", 4.0)
    
    system.delete_student(102)
    assert system.current_size == 2
    # Verify User C shifted to index 1
    assert system.get_all_records()[1].student_id == 103

def test_delete_non_existent(system):
    """Ensure proper error handling for missing IDs."""
    with pytest.raises(KeyError):
        system.delete_student(999)

def test_capacity_limit(system):
    """Verify system enforces memory bounds."""
    for i in range(5):
        system.create_student(i, f"Student {i}", 3.0)
    
    with pytest.raises(MemoryError, match="capacity reached"):
        system.create_student(6, "Extra Student", 3.0)

def test_read_non_existent(system):
    """Ensure KeyError on invalid read."""
    with pytest.raises(KeyError):
        system.read_student(500)
