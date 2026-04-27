import pytest
from blockchain_simulation import Blockchain

def test_blockchain_integrity():
    bc = Blockchain()
    bc.add_block("Transaction 1")
    bc.add_block("Transaction 2")
    
    assert bc.is_chain_valid() is True

def test_tamper_detection():
    bc = Blockchain()
    bc.add_block("Secret Data")
    
    # Simulate tampering
    bc._chain[1].data = "Hacked Data"
    
    # Chain should now be invalid
    assert bc.is_chain_valid() is False

def test_linkage_integrity():
    bc = Blockchain()
    bc.add_block("Block 1")
    bc.add_block("Block 2")
    
    # Corrupt a hash in the middle
    bc._chain[1].hash = "fakehash"
    
    assert bc.is_chain_valid() is False
