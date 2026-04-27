from typing import List, Dict, Optional, Final

class TrieNode:
    """Represents a single character node in the Prefix Tree."""
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False

class AutocompleteEngine:
    """
    Enterprise-grade Autocomplete System using a Trie (Prefix Tree).
    
    Attributes:
        _root (TrieNode): The entry point of the prefix tree.
    """

    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        
        Time Complexity: O(L) where L is the word length.
        Space Complexity: O(L) in the worst case (no prefix overlap).
        """
        if not word:
            return

        current = self._root
        # Normalize to lowercase for consistent search
        for char in word.lower().strip():
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        current.is_end_of_word = True

    def search_prefix(self, prefix: str) -> List[str]:
        """
        Returns all words that start with the given prefix.
        
        Time Complexity: O(L + S) where L is prefix length and S is total nodes in sub-tree.
        Space Complexity: O(S) for the result list.
        """
        if not prefix:
            return []

        current = self._root
        prefix = prefix.lower().strip()

        # Step 1: Navigate to the end of the prefix
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        # Step 2: Perform DFS from the prefix node to find all suffixes
        suggestions: List[str] = []
        self._dfs_collect(current, prefix, suggestions)
        return suggestions

    def _dfs_collect(self, node: TrieNode, path: str, results: List[str]) -> None:
        """Helper to collect all words starting from a given node."""
        if node.is_end_of_word:
            results.append(path)

        # Explore children in alphabetical order for deterministic output
        for char in sorted(node.children.keys()):
            self._dfs_collect(node.children[char], path + char, results)

    def bulk_insert(self, words: List[str]) -> None:
        """Optimized insertion for large datasets."""
        for word in words:
            self.insert(word)
