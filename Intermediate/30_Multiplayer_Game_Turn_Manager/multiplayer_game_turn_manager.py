from collections import deque
from typing import List, Optional

class TurnManager:
    """
    Multiplayer Game Turn Manager using a Circular Queue.
    """

    def __init__(self, players: List[str]):
        if not players:
            raise ValueError("Player list cannot be empty.")
        self._queue: deque[str] = deque(players)

    def next_turn(self) -> str:
        """
        Rotates the queue and returns the next player.
        Time Complexity: O(1)
        """
        player = self._queue.popleft()
        self._queue.append(player)
        return player

    def add_player(self, name: str) -> None:
        """Adds a player to the end of the rotation."""
        self._queue.append(name)

    def remove_player(self, name: str) -> bool:
        """Removes a player from the rotation."""
        try:
            self._queue.remove(name)
            return True
        except ValueError:
            return False

    @property
    def current_player(self) -> str:
        return self._queue[0]

    @property
    def player_count(self) -> int:
        return len(self._queue)
