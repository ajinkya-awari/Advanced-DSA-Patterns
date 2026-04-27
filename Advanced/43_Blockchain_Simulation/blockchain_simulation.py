import hashlib
import time
from typing import List, Optional, Final

class Block:
    """Represents a single block in the chain."""
    def __init__(self, index: int, data: str, prev_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self._calculate_hash()

    def _calculate_hash(self) -> str:
        payload = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(payload.encode()).hexdigest()

class Blockchain:
    """
    Enterprise-grade Blockchain Simulation using Hash-Linked Lists.
    """

    def __init__(self):
        self._chain: List[Block] = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        return Block(0, "Genesis Block", "0")

    def add_block(self, data: str) -> Block:
        """Appends a new block linked to the previous one."""
        prev_block = self._chain[-1]
        new_block = Block(len(self._chain), data, prev_block.hash)
        self._chain.append(new_block)
        return new_block

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the entire chain.
        Time Complexity: O(N)
        """
        for i in range(1, len(self._chain)):
            current = self._chain[i]
            previous = self._chain[i-1]
            
            # Check if block's own hash is corrupted
            if current.hash != current._calculate_hash():
                return False
                
            # Check linkage
            if current.prev_hash != previous.hash:
                return False
                
        return True

    @property
    def last_block(self) -> Block:
        return self._chain[-1]
