from typing import List, Set

class Elevator:
    """
    Elevator Simulator using a directional scanning strategy.
    """

    def __init__(self, floors: int):
        self._floors = floors
        self._current_floor = 0
        self._direction = 1 # 1 for up, -1 for down
        self._requests: Set[int] = set()

    def request_floor(self, floor: int) -> None:
        if 0 <= floor < self._floors:
            self._requests.add(floor)

    def process_all_requests(self) -> List[int]:
        """
        Simulates the SCAN algorithm to process requests.
        """
        log = []
        while self._requests:
            # Get requests in current direction
            targets = [f for f in self._requests if (f - self._current_floor) * self._direction >= 0]
            
            if not targets:
                # Switch direction if no more targets in current path
                self._direction *= -1
                continue

            # Pick nearest in direction
            next_floor = min(targets) if self._direction == 1 else max(targets)
            
            # Simulate travel
            while self._current_floor != next_floor:
                self._current_floor += self._direction
                if self._current_floor in self._requests:
                    log.append(self._current_floor)
                    self._requests.remove(self._current_floor)
        
        return log
