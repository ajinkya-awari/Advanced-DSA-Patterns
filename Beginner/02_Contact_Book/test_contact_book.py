import pytest
from contact_book import ContactBook

@pytest.fixture
def contact_book():
    return ContactBook()

def test_insertion_o1(contact_book):
    """Verify O(1) insertion at head."""
    contact_book.insert_contact("Alice", "123", "alice@test.com")
    contact_book.insert_contact("Bob", "456", "bob@test.com")
    
    assert contact_book.total_contacts == 2
    # Bob should be head as it was inserted last
    assert contact_book.find_contact("Bob").name == "Bob"

def test_search_happy_path(contact_book):
    """Verify O(N) search functionality."""
    contact_book.insert_contact("Charlie", "789", "charlie@test.com")
    result = contact_book.find_contact("Charlie")
    assert result is not None
    assert result.phone_number == "789"

def test_search_non_existent(contact_book):
    """Verify search returns None for missing contacts."""
    assert contact_book.find_contact("Ghost") is None

def test_update_contact(contact_book):
    """Verify contact field updates."""
    contact_book.insert_contact("David", "111", "david@test.com")
    contact_book.update_contact("David", new_phone="999")
    assert contact_book.find_contact("David").phone_number == "999"

def test_delete_head(contact_book):
    """Verify deletion of the first node."""
    contact_book.insert_contact("A", "1", "a@a.com")
    contact_book.insert_contact("B", "2", "b@b.com")
    contact_book.delete_contact("B")
    assert contact_book.total_contacts == 1
    assert contact_book.find_contact("B") is None

def test_delete_middle_or_tail(contact_book):
    """Verify deletion of subsequent nodes."""
    contact_book.insert_contact("A", "1", "a@a.com")
    contact_book.insert_contact("B", "2", "b@b.com")
    contact_book.insert_contact("C", "3", "c@c.com")
    
    contact_book.delete_contact("A") # Tail
    assert contact_book.total_contacts == 2
    assert contact_book.find_contact("A") is None

def test_delete_empty_or_missing(contact_book):
    """Verify error handling for invalid deletions."""
    with pytest.raises(KeyError):
        contact_book.delete_contact("Empty")
