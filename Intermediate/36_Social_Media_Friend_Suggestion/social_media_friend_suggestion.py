from typing import Dict, Set, List, Tuple
from collections import Counter

class SocialGraph:
    """
    Social Media Friend Suggestion Engine using Graph Traversal.
    """

    def __init__(self):
        self._adj: Dict[str, Set[str]] = {}

    def add_friendship(self, user1: str, user2: str) -> None:
        if user1 not in self._adj: self._adj[user1] = set()
        if user2 not in self._adj: self._adj[user2] = set()
        self._adj[user1].add(user2)
        self._adj[user2].add(user1)

    def suggest_friends(self, user: str) -> List[Tuple[str, int]]:
        """
        Suggests friends based on mutual connections (2nd degree).
        Returns list of (username, mutual_count) sorted by count.
        """
        if user not in self._adj:
            return []

        my_friends = self._adj[user]
        suggestions = Counter()

        for friend in my_friends:
            for potential_friend in self._adj[friend]:
                if potential_friend != user and potential_friend not in my_friends:
                    suggestions[potential_friend] += 1
        
        return suggestions.most_common()
