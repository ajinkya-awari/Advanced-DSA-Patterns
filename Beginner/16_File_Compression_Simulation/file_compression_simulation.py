import heapq
from typing import Dict, List, Optional, Tuple, Final
from dataclasses import dataclass, field

@dataclass
class HuffmanNode:
    """A node in the Huffman Tree."""
    char: Optional[str] = None
    freq: int = 0
    left: Optional['HuffmanNode'] = None
    right: Optional['HuffmanNode'] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq

class HuffmanCoding:
    """
    Enterprise-grade Huffman Coding implementation for file compression.
    """

    def __init__(self):
        self._encoding_map: Dict[str, str] = {}
        self._decoding_map: Dict[str, str] = {}
        self._root: Optional[HuffmanNode] = None

    def _build_tree(self, text: str) -> Optional[HuffmanNode]:
        """Constructs the Huffman Tree from character frequencies."""
        if not text:
            return None

        # Frequency analysis: O(N)
        frequency: Dict[str, int] = {}
        for char in text:
            frequency[char] = frequency.get(char, 0) + 1

        # Min-Priority Queue initialization: O(K log K)
        priority_queue: List[HuffmanNode] = [
            HuffmanNode(char=char, freq=freq) for char, freq in frequency.items()
        ]
        heapq.heapify(priority_queue)

        # Handle edge case: single unique character
        if len(priority_queue) == 1:
            node = heapq.heappop(priority_queue)
            parent = HuffmanNode(freq=node.freq, left=node)
            return parent

        # Greedy tree construction: O(K log K)
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            
            parent = HuffmanNode(
                freq=left.freq + right.freq,
                left=left,
                right=right
            )
            heapq.heappush(priority_queue, parent)

        return heapq.heappop(priority_queue)

    def _generate_codes(self, node: Optional[HuffmanNode], current_code: str) -> None:
        """Traverses the tree to generate binary codes."""
        if not node:
            return

        if node.char is not None:
            self._encoding_map[node.char] = current_code
            self._decoding_map[current_code] = node.char
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def compress(self, text: str) -> str:
        """
        Compresses input text into a Huffman-coded bit string.
        Time Complexity: O(N + K log K)
        Space Complexity: O(K) for the tree
        """
        if not text:
            return ""

        self._root = self._build_tree(text)
        self._encoding_map = {}
        self._generate_codes(self._root, "")

        return "".join(self._encoding_map[char] for char in text)

    def decompress(self, encoded_text: str) -> str:
        """
        Decompresses a bit string back into the original text.
        Time Complexity: O(N)
        """
        if not encoded_text or not self._root:
            return ""

        result: List[str] = []
        current_node = self._root
        
        for bit in encoded_text:
            if not current_node:
                break
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            
            if current_node and current_node.char is not None:
                result.append(current_node.char)
                current_node = self._root
                
        return "".join(result)

    def get_compression_ratio(self, original_text: str, encoded_text: str) -> float:
        """Calculates ratio (Original Size / Compressed Size)."""
        if not original_text:
            return 0.0
        # Original: 8 bits per character. Compressed: 1 bit per 'bit' in string.
        original_size = len(original_text) * 8
        compressed_size = len(encoded_text)
        return original_size / compressed_size if compressed_size > 0 else 0.0
