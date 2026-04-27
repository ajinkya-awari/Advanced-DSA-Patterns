import pytest
from memory_allocation_simulator import MemorySimulator

def test_memory_allocation():
    mem = MemorySimulator(100)
    addr1 = mem.malloc(20)
    addr2 = mem.malloc(30)
    assert addr1 == 0
    assert addr2 == 20
    mem.free(addr1)
    addr3 = mem.malloc(10) # Best fit should ideally pick the 20-block
    assert addr3 == 0
