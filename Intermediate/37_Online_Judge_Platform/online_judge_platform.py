import heapq
from typing import Dict, List, Tuple

class OnlineJudgeLeaderboard:
    """
    Real-time leaderboard for an Online Judge using a Max-Heap.
    """

    def __init__(self):
        self._user_scores: Dict[str, int] = {}
        # Elements: (-score, user_id) for max-heap behavior
        self._heap: List[Tuple[int, str]] = []

    def update_score(self, user_id: str, points: int) -> None:
        """Adds points to a user's score and updates the leaderboard."""
        new_score = self._user_scores.get(user_id, 0) + points
        self._user_scores[user_id] = new_score
        heapq.heappush(self._heap, (-new_score, user_id))

    def get_top_k(self, k: int) -> List[Tuple[str, int]]:
        """
        Returns top K users. 
        Note: Since we use lazy updates in the heap, we filter duplicates.
        """
        result = []
        temp_heap = list(self._heap)
        seen = set()
        
        while temp_heap and len(result) < k:
            neg_score, user_id = heapq.heappop(temp_heap)
            if user_id not in seen:
                seen.add(user_id)
                # Verify if this is the latest score
                if -neg_score == self._user_scores[user_id]:
                    result.append((user_id, -neg_score))
        return result
