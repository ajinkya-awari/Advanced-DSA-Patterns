import pytest
from phone_directory import PhoneDirectory

@pytest.fixture
def directory():
    return PhoneDirectory()

def test_add_and_get_contact(directory):
    """Verify O(1) insertion and retrieval."""
    directory.add_contact("John Doe", "1234567890")
    contact = directory.get_contact("John Doe")
    assert contact.name == "John Doe"
    assert contact.phone_number == "1234567890"

def test_case_insensitivity(directory):
    """Verify that retrieval is case-insensitive."""
    directory.add_contact("Alice", "999")
    assert directory.get_contact("alice").phone_number == "999"

def test_duplicate_prevention(directory):
    """Verify that duplicate names are rejected."""
    directory.add_contact("Bob", "111")
    with pytest.raises(ValueError, match="already exists"):
        directory.add_contact("BOB", "222")

def test_update_contact(directory):
    """Verify field updates."""
    directory.add_contact("Charlie", "555")
    directory.update_contact("Charlie", "777")
    assert directory.get_contact("Charlie").phone_number == "777"

def test_delete_contact(directory):
    """Verify contact removal."""
    directory.add_contact("DeleteMe", "000")
    directory.delete_contact("DeleteMe")
    assert directory.total_contacts == 0
    with pytest.raises(KeyError):
        directory.get_contact("DeleteMe")

def test_invalid_operations(directory):
    """Verify error handling for missing keys or empty inputs."""
    with pytest.raises(ValueError, match="cannot be empty"):
        directory.add_contact(" ", "123")
    
    with pytest.raises(KeyError):
        directory.update_contact("Ghost", "123")
