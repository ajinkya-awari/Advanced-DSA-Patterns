import pytest
from file_compression_simulation import HuffmanCoding

@pytest.fixture
def huffman():
    return HuffmanCoding()

def test_basic_compression_decompression(huffman):
    """Verify standard cycle of compression and recovery."""
    original = "hello world"
    encoded = huffman.compress(original)
    decoded = huffman.decompress(encoded)
    
    assert decoded == original
    assert len(encoded) < (len(original) * 8)

def test_single_char_redundancy(huffman):
    """Verify high compression for highly redundant data."""
    original = "aaaaa"
    encoded = huffman.compress(original)
    decoded = huffman.decompress(encoded)
    
    assert decoded == original
    # For single unique char, we expect 1 bit per char in our implementation
    assert len(encoded) == 5 

def test_empty_string(huffman):
    """Verify robustness against empty inputs."""
    assert huffman.compress("") == ""
    assert huffman.decompress("") == ""

def test_complex_string(huffman):
    """Verify reliability with diverse character sets."""
    original = "Huffman coding is a greedy algorithm for lossless data compression!"
    encoded = huffman.compress(original)
    decoded = huffman.decompress(encoded)
    assert decoded == original

def test_compression_ratio(huffman):
    """Verify that ratio calculation works and indicates efficiency."""
    original = "test" # 32 bits
    encoded = huffman.compress(original) # usually < 32 bits
    ratio = huffman.get_compression_ratio(original, encoded)
    assert ratio > 1.0
