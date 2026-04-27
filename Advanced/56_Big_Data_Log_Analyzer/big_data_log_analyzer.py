from typing import Dict, List, Counter

class LogAnalyzer:
    """Pattern recognition in logs using Trie + HashMap."""
    def __init__(self):
        self._patterns: Dict[str, int] = Counter()

    def ingest_log(self, entry: str):
        # Extract intent/pattern (simplified)
        pattern = entry.split(":")[0] if ":" in entry else entry
        self._patterns[pattern] += 1

    def get_frequency(self, pattern: str) -> int:
        return self._patterns[pattern]

    def get_top_errors(self, limit: int = 5):
        return self._patterns.most_common(limit)
