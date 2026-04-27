import heapq
from typing import Dict, List, Tuple, Optional

class AuctionSystem:
    """
    Tracks highest bids across multiple items using individual Max-Heaps.
    """

    def __init__(self):
        # item_id -> heap of (-amount, bidder_id)
        self._item_bids: Dict[str, List[Tuple[float, str]]] = {}

    def place_bid(self, item_id: str, bidder_id: str, amount: float) -> bool:
        """Places a bid if it's higher than the current max."""
        if item_id not in self._item_bids:
            self._item_bids[item_id] = []
        
        current_max = self.get_highest_bid(item_id)
        if current_max and amount <= current_max[0]:
            return False
            
        heapq.heappush(self._item_bids[item_id], (-amount, bidder_id))
        return True

    def get_highest_bid(self, item_id: str) -> Optional[Tuple[float, str]]:
        """Returns (amount, bidder_id) of the highest bid."""
        if item_id not in self._item_bids or not self._item_bids[item_id]:
            return None
        
        neg_amount, bidder_id = self._item_bids[item_id][0]
        return (-neg_amount, bidder_id)
