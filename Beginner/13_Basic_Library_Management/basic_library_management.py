from typing import List, Optional, Final
from dataclasses import dataclass

@dataclass
class Book:
    """Represents a book entity in the library."""
    isbn: str
    title: str
    author: str
    is_checked_out: bool = False

class LibraryManager:
    """
    Enterprise-grade Library Management System using contiguous arrays.
    
    Attributes:
        _capacity (int): Maximum books the library can house.
        _books (List[Optional[Book]]): The underlying array structure.
        _count (int): Current number of books in the catalog.
    """

    def __init__(self, capacity: int = 1000):
        self._capacity: Final[int] = capacity
        self._books: List[Optional[Book]] = [None] * capacity
        self._count: int = 0

    def _find_index(self, isbn: str) -> int:
        """
        Locates the array index of a book by ISBN.
        Time Complexity: O(N)
        """
        for i in range(self._count):
            if self._books[i] and self._books[i].isbn == isbn:
                return i
        return -1

    def add_book(self, isbn: str, title: str, author: str) -> None:
        """
        Adds a new book to the catalog.
        Time Complexity: O(N) due to uniqueness check.
        """
        if self._count >= self._capacity:
            raise MemoryError("Library storage is at maximum capacity.")
        
        if self._find_index(isbn) != -1:
            raise ValueError(f"Book with ISBN {isbn} already exists in the catalog.")

        self._books[self._count] = Book(isbn, title, author)
        self._count += 1

    def remove_book(self, isbn: str) -> bool:
        """
        Removes a book and shifts elements to maintain contiguity.
        Time Complexity: O(N)
        """
        index = self._find_index(isbn)
        if index == -1:
            raise KeyError(f"ISBN {isbn} not found.")

        # Shift left to fill gap
        for i in range(index, self._count - 1):
            self._books[i] = self._books[i + 1]
        
        self._books[self._count - 1] = None
        self._count -= 1
        return True

    def checkout_book(self, isbn: str) -> bool:
        """
        Marks a book as checked out.
        Time Complexity: O(N)
        """
        index = self._find_index(isbn)
        if index == -1:
            raise KeyError(f"ISBN {isbn} not found.")
        
        book = self._books[index]
        if book.is_checked_out:
            raise RuntimeError(f"Book '{book.title}' is already checked out.")
        
        book.is_checked_out = True
        return True

    def return_book(self, isbn: str) -> bool:
        """
        Marks a checked-out book as available.
        Time Complexity: O(N)
        """
        index = self._find_index(isbn)
        if index == -1:
            raise KeyError(f"ISBN {isbn} not found.")
        
        book = self._books[index]
        if not book.is_checked_out:
            raise RuntimeError(f"Book '{book.title}' was not checked out.")
        
        book.is_checked_out = False
        return True

    def get_book_details(self, isbn: str) -> Book:
        """Retrieves book metadata by ISBN."""
        index = self._find_index(isbn)
        if index == -1:
            raise KeyError(f"ISBN {isbn} not found.")
        return self._books[index]

    @property
    def total_books(self) -> int:
        return self._count
