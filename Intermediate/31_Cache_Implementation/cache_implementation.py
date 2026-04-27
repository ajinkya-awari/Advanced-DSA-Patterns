from typing import Dict, Optional

class Node:
    """Doubly Linked List node for LRU order tracking."""
    def __init__(self, key: int, value: int):
        self.key: int = key
        self.value: int = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class LRUCache:
    """
    Enterprise-grade LRU Cache using HashMap + Doubly Linked List.
    All operations are O(1) time complexity.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity: int = capacity
        self._cache: Dict[int, Node] = {}
        
        # Sentinel dummy nodes to avoid null checks
        self._head: Node = Node(0, 0)
        self._tail: Node = Node(0, 0)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: Node) -> None:
        """Removes a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node) -> None:
        """Adds a node immediately after the head sentinel."""
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node

    def get(self, key: int) -> int:
        """
        Retrieves a value and moves the key to the most-recent position.
        Time Complexity: O(1)
        """
        if key not in self._cache:
            return -1
        
        node = self._cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a value. Evicts LRU if capacity is exceeded.
        Time Complexity: O(1)
        """
        if key in self._cache:
            self._remove(self._cache[key])
        
        new_node = Node(key, value)
        self._add_to_front(new_node)
        self._cache[key] = new_node

        if len(self._cache) > self._capacity:
            # Evict from tail (before sentinel)
            lru_node = self._tail.prev
            self._remove(lru_node)
            del self._cache[lru_node.key]
