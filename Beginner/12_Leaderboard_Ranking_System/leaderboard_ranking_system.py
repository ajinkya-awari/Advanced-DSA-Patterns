from typing import List, Dict, Optional, Final
from dataclasses import dataclass

@dataclass
class PlayerRecord:
    """Represents a player's standing on the leaderboard."""
    player_id: str
    score: int

    def __lt__(self, other: 'PlayerRecord') -> bool:
        # Custom comparison for descending scores, then ascending ID
        if self.score != other.score:
            return self.score > other.score
        return self.player_id < other.player_id

class Leaderboard:
    """
    Enterprise-grade Leaderboard System optimized for Top-K updates.
    
    Attributes:
        _sorted_ranks (List[PlayerRecord]): Contiguous array maintaining sorted order.
        _registry (Dict[str, int]): Hash Map for O(1) score lookups.
    """

    def __init__(self):
        self._sorted_ranks: List[PlayerRecord] = []
        self._registry: Dict[str, int] = {}

    def update_score(self, player_id: str, new_score: int) -> None:
        """
        Updates or creates a player's score and re-ranks them.
        
        Time Complexity: O(N) due to array shifting.
        Space Complexity: O(1)
        """
        if player_id in self._registry:
            # Remove old record to maintain invariant
            old_score = self._registry[player_id]
            self._remove_record(player_id, old_score)

        # Insert new record
        new_record = PlayerRecord(player_id, new_score)
        self._insert_record(new_record)
        self._registry[player_id] = new_score

    def _insert_record(self, record: PlayerRecord) -> None:
        """Internal helper to insert a record into the sorted list using binary search."""
        low, high = 0, len(self._sorted_ranks)
        while low < high:
            mid = (low + high) // 2
            if record < self._sorted_ranks[mid]:
                high = mid
            else:
                low = mid + 1
        self._sorted_ranks.insert(low, record)

    def _remove_record(self, player_id: str, score: int) -> None:
        """Internal helper to remove a record by searching its expected position."""
        target = PlayerRecord(player_id, score)
        low, high = 0, len(self._sorted_ranks)
        idx = -1
        while low < high:
            mid = (low + high) // 2
            if self._sorted_ranks[mid].player_id == player_id and self._sorted_ranks[mid].score == score:
                idx = mid
                break
            if target < self._sorted_ranks[mid]:
                high = mid
            else:
                low = mid + 1
        
        if idx != -1:
            self._sorted_ranks.pop(idx)

    def get_top_k(self, k: int) -> List[PlayerRecord]:
        """
        Retrieves the top K players.
        
        Time Complexity: O(K)
        """
        return self._sorted_ranks[:k]

    def get_rank(self, player_id: str) -> Optional[int]:
        """
        Retrieves the 1-based rank of a player.
        
        Time Complexity: O(N) worst case search.
        """
        if player_id not in self._registry:
            return None
        
        for i, record in enumerate(self._sorted_ranks):
            if record.player_id == player_id:
                return i + 1
        return None

    @property
    def total_players(self) -> int:
        return len(self._sorted_ranks)
