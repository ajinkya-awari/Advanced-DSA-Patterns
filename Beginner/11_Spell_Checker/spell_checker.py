from typing import List, Optional, Final

class HashNode:
    """Represents a node in the collision chain."""
    def __init__(self, key: str):
        self.key: str = key
        self.next: Optional['HashNode'] = None

class SpellChecker:
    """
    Enterprise-grade Spell Checker using a custom Hash Table with Chaining.
    
    Attributes:
        _capacity (int): Number of buckets in the hash table.
        _size (int): Total number of words stored.
        _buckets (List[Optional[HashNode]]): The hash table array.
    """

    INITIAL_CAPACITY: Final[int] = 101
    LOAD_FACTOR_THRESHOLD: Final[float] = 0.75
    PRIME_MULTIPLIER: Final[int] = 31

    def __init__(self):
        self._capacity = self.INITIAL_CAPACITY
        self._size = 0
        self._buckets: List[Optional[HashNode]] = [None] * self._capacity

    def _get_hash(self, key: str, capacity: Optional[int] = None) -> int:
        """
        Polynomial Rolling Hash Function.
        Time Complexity: O(L) where L is string length.
        """
        h = 0
        cap = capacity or self._capacity
        for char in key:
            h = (h * self.PRIME_MULTIPLIER + ord(char)) % cap
        return h

    def _resize(self) -> None:
        """
        Doubles the capacity and rehashes all existing keys.
        Time Complexity: O(N + K) where N is words and K is capacity.
        """
        new_capacity = self._capacity * 2
        new_buckets: List[Optional[HashNode]] = [None] * new_capacity

        for head in self._buckets:
            current = head
            while current:
                new_h = self._get_hash(current.key, new_capacity)
                # Insert into new bucket structure
                new_node = HashNode(current.key)
                new_node.next = new_buckets[new_h]
                new_buckets[new_h] = new_node
                current = current.next

        self._capacity = new_capacity
        self._buckets = new_buckets

    def add_word(self, word: str) -> None:
        """
        Adds a word to the dictionary.
        Time Complexity: O(L) average, O(N) worst-case (rare due to resizing).
        """
        word = word.lower().strip()
        if not word or self.check_word(word):
            return

        if (self._size / self._capacity) >= self.LOAD_FACTOR_THRESHOLD:
            self._resize()

        h = self._get_hash(word)
        new_node = HashNode(word)
        new_node.next = self._buckets[h]
        self._buckets[h] = new_node
        self._size += 1

    def check_word(self, word: str) -> bool:
        """
        Checks if a word exists in the dictionary.
        Time Complexity: O(L) average.
        """
        word = word.lower().strip()
        h = self._get_hash(word)
        current = self._buckets[h]
        
        while current:
            if current.key == word:
                return True
            current = current.next
        return False

    @property
    def dictionary_size(self) -> int:
        return self._size

    @property
    def current_capacity(self) -> int:
        return self._capacity
