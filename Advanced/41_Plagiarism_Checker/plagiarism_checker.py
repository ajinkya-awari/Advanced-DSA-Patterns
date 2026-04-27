from typing import Set, List, Final

class PlagiarismChecker:
    """
    Advanced Plagiarism Checker using the Rabin-Karp Rolling Hash algorithm.
    Detects identical substrings of a fixed window size (shingles).
    """

    PRIME: Final[int] = 10**9 + 7
    BASE: Final[int] = 256

    def __init__(self, window_size: int = 10):
        self._window_size = window_size

    def _get_hashes(self, text: str) -> Set[int]:
        """Calculates rolling hashes for all shingles in the text."""
        if len(text) < self._window_size:
            return set()

        hashes = set()
        n = len(text)
        m = self._window_size
        
        # Calculate high-order weight (BASE^(m-1) % PRIME)
        h = 1
        for _ in range(m - 1):
            h = (h * self.BASE) % self.PRIME

        # Initial hash
        current_hash = 0
        for i in range(m):
            current_hash = (self.BASE * current_hash + ord(text[i])) % self.PRIME
        
        hashes.add(current_hash)

        # Rolling hash
        for i in range(n - m):
            current_hash = (self.BASE * (current_hash - ord(text[i]) * h) + ord(text[i + m])) % self.PRIME
            # Handle negative result
            if current_hash < 0:
                current_hash += self.PRIME
            hashes.add(current_hash)
            
        return hashes

    def check_similarity(self, doc1: str, doc2: str) -> float:
        """
        Calculates Jaccard Similarity based on shingle hashes.
        Time Complexity: O(N + M)
        Space Complexity: O(N + M)
        """
        hashes1 = self._get_hashes(doc1)
        hashes2 = self._get_hashes(doc2)

        if not hashes1 or not hashes2:
            return 0.0

        intersection = hashes1.intersection(hashes2)
        union = hashes1.union(hashes2)
        
        return len(intersection) / len(union)
