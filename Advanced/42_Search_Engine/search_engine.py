from typing import List, Dict, Set, Tuple, Optional
from collections import Counter

class SearchNode:
    def __init__(self):
        self.children: Dict[str, 'SearchNode'] = {}
        # doc_id -> frequency
        self.doc_frequencies: Counter = Counter()

class SearchEngine:
    """
    Advanced Search Engine using a Trie for indexing and term frequency ranking.
    """

    def __init__(self):
        self._root = SearchNode()
        self._doc_titles: Dict[str, str] = {}

    def index_document(self, doc_id: str, title: str, content: str) -> None:
        """Indexes tokens from a document into the Trie."""
        self._doc_titles[doc_id] = title
        tokens = content.lower().split()
        
        for token in tokens:
            current = self._root
            for char in token:
                if char not in current.children:
                    current.children[char] = SearchNode()
                current = current.children[char]
            current.doc_frequencies[doc_id] += 1

    def search(self, query: str) -> List[Tuple[str, int]]:
        """
        Returns doc titles and frequencies, ranked by relevance.
        Time Complexity: O(L) where L is query length.
        """
        tokens = query.lower().split()
        if not tokens: return []
        
        # For simplicity, we search for the first term
        target_token = tokens[0]
        current = self._root
        for char in target_token:
            if char not in current.children:
                return []
            current = current.children[char]
            
        results = []
        for doc_id, freq in current.doc_frequencies.most_common():
            results.append((self._doc_titles[doc_id], freq))
        return results
