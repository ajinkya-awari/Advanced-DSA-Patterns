from typing import Set, List

class SpamFilter:
    """Intent-based spam filtering using Hashing."""
    def __init__(self, blacklist: List[str]):
        self._blacklist: Set[str] = set(word.lower() for word in blacklist)

    def get_spam_score(self, email_body: str) -> float:
        tokens = email_body.lower().split()
        if not tokens: return 0.0
        matches = sum(1 for token in tokens if token in self._blacklist)
        return matches / len(tokens)

    def is_spam(self, email_body: str, threshold: float = 0.1) -> bool:
        return self.get_spam_score(email_body) >= threshold
