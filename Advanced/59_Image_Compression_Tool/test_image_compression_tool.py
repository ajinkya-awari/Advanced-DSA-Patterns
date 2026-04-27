import pytest
from image_compression_tool import ImageCompressor

def test_image_compression():
    pixels = [255, 255, 0, 0, 0, 128]
    ic = ImageCompressor(pixels)
    codes = ic.compress()
    assert len(codes[0]) < len(codes[128]) # Most frequent (0) should have shortest code
