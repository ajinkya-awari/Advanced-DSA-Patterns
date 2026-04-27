from typing import List, Dict, Optional, Final
from dataclasses import dataclass

@dataclass
class WordDefinition:
    """Represents a word and its metadata."""
    word: str
    definition: str
    part_of_speech: str

class TrieNode:
    """Represents a node in the prefix tree."""
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False

class DictionaryApp:
    """
    Enterprise-grade Dictionary Application combining HashMap and Trie.
    
    Attributes:
        _lookup_table (Dict[str, WordDefinition]): O(1) storage for definitions.
        _prefix_tree (TrieNode): O(L) storage for word discovery.
    """

    def __init__(self):
        self._lookup_table: Dict[str, WordDefinition] = {}
        self._prefix_tree: TrieNode = TrieNode()

    def _normalize(self, text: str) -> str:
        """Internal helper for consistent key formatting."""
        return text.strip().lower()

    def add_word(self, word: str, definition: str, part_of_speech: str) -> None:
        """
        Adds a word to both the Trie and the HashMap.
        
        Time Complexity: O(L) where L is word length.
        Space Complexity: O(L) for new nodes/entries.
        """
        if not word or not definition:
            raise ValueError("Word and definition cannot be empty.")

        normalized_word = self._normalize(word)
        
        # 1. Update Hash Map for O(1) lookup
        self._lookup_table[normalized_word] = WordDefinition(
            word=word.strip(),
            definition=definition.strip(),
            part_of_speech=part_of_speech.strip()
        )

        # 2. Update Trie for prefix discovery
        current = self._prefix_tree
        for char in normalized_word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def get_definition(self, word: str) -> Optional[WordDefinition]:
        """
        Retrieves the definition of a specific word.
        
        Time Complexity: O(1) average.
        """
        return self._lookup_table.get(self._normalize(word))

    def suggest_words(self, prefix: str) -> List[str]:
        """
        Finds all words starting with the given prefix.
        
        Time Complexity: O(L + K) where L is prefix length and K is sub-tree size.
        """
        normalized_prefix = self._normalize(prefix)
        if not normalized_prefix:
            return []

        current = self._prefix_tree
        for char in normalized_prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        results: List[str] = []
        self._dfs_collect(current, normalized_prefix, results)
        return results

    def _dfs_collect(self, node: TrieNode, path: str, results: List[str]) -> None:
        """Recursive DFS to collect all valid word terminations."""
        if node.is_end_of_word:
            results.append(path)

        for char in sorted(node.children.keys()):
            self._dfs_collect(node.children[char], path + char, results)

    def delete_word(self, word: str) -> bool:
        """
        Removes a word from the dictionary.
        Note: For simplicity, this removes from HashMap and marks Trie node as not end-of-word.
        """
        normalized_word = self._normalize(word)
        if normalized_word not in self._lookup_table:
            return False

        # Remove from O(1) table
        del self._lookup_table[normalized_word]

        # De-mark in Trie
        current = self._prefix_tree
        for char in normalized_word:
            if char not in current.children:
                return False
            current = current.children[char]
        current.is_end_of_word = False
        return True

    @property
    def vocabulary_size(self) -> int:
        return len(self._lookup_table)
