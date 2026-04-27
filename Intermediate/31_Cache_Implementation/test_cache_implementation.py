import pytest
from cache_implementation import LRUCache

def test_lru_operations():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)    # Evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)    # Evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

def test_update_existing():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10
