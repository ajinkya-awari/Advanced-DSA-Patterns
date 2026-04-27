import pytest
from basic_library_management import LibraryManager, Book

@pytest.fixture
def library():
    return LibraryManager(capacity=10)

def test_add_book(library):
    """Verify successful catalog entry."""
    library.add_book("123-456", "Clean Code", "Robert Martin")
    assert library.total_books == 1
    assert library.get_book_details("123-456").title == "Clean Code"

def test_duplicate_isbn(library):
    """Verify protection against duplicate entries."""
    library.add_book("123", "Book A", "Author A")
    with pytest.raises(ValueError, match="already exists"):
        library.add_book("123", "Book B", "Author B")

def test_checkout_return_cycle(library):
    """Verify state transition logic."""
    library.add_book("123", "Test Book", "Author")
    
    # Checkout
    library.checkout_book("123")
    assert library.get_book_details("123").is_checked_out is True
    
    # Check out again should fail
    with pytest.raises(RuntimeError, match="already checked out"):
        library.checkout_book("123")
        
    # Return
    library.return_book("123")
    assert library.get_book_details("123").is_checked_out is False

def test_remove_and_shift(library):
    """Verify array contiguity after deletion."""
    library.add_book("1", "A", "Auth")
    library.add_book("2", "B", "Auth")
    library.add_book("3", "C", "Auth")
    
    library.remove_book("2")
    assert library.total_books == 2
    # ISBN 3 should now be at index 1
    assert library.get_book_details("3").isbn == "3"

def test_invalid_isbn_operations(library):
    """Verify error handling for missing books."""
    with pytest.raises(KeyError):
        library.checkout_book("999")
    with pytest.raises(KeyError):
        library.remove_book("999")

def test_capacity_overflow(library):
    """Verify memory bounds enforcement."""
    lib = LibraryManager(capacity=2)
    lib.add_book("1", "A", "A")
    lib.add_book("2", "B", "B")
    with pytest.raises(MemoryError, match="maximum capacity"):
        lib.add_book("3", "C", "C")
