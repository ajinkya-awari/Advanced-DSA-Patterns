import heapq
from typing import Dict, List, Optional

class HuffmanNode:
    def __init__(self, pixel: Optional[int], freq: int):
        self.pixel = pixel
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other): return self.freq < other.freq

class ImageCompressor:
    """Simulated Image compression using pixel Huffman encoding."""
    def __init__(self, pixels: List[int]):
        self.pixels = pixels
        self.codes = {}

    def compress(self) -> Dict[int, str]:
        freq = {}
        for p in self.pixels: freq[p] = freq.get(p, 0) + 1
        heap = [HuffmanNode(p, f) for p, f in freq.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            l, r = heapq.heappop(heap), heapq.heappop(heap)
            node = HuffmanNode(None, l.freq + r.freq)
            node.left, node.right = l, r
            heapq.heappush(heap, node)
        
        if heap: self._gen_codes(heap[0], "")
        return self.codes

    def _gen_codes(self, node, code):
        if node.pixel is not None:
            self.codes[node.pixel] = code
            return
        self._gen_codes(node.left, code + "0")
        self._gen_codes(node.right, code + "1")
