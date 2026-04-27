from collections import deque
import re

class PalindromeChecker:
    """
    Enterprise-grade Palindrome validation utility using Deque structures.
    """

    @staticmethod
    def is_palindrome(input_text: str) -> bool:
        """
        Determines if a string is a palindrome using bidirectional deque comparison.
        
        Time Complexity: O(N) where N is the length of the input string.
        Space Complexity: O(N) to store sanitized characters in the deque.
        """
        if input_text is None:
            return False
            
        # Preprocessing: Remove non-alphanumeric and normalize case
        sanitized_text = re.sub(r'[^a-zA-Z0-9]', '', input_text).lower()
        
        if len(sanitized_text) <= 1:
            return True

        char_deque: deque[str] = deque(sanitized_text)

        # Compare from both ends simultaneously
        while len(char_deque) > 1:
            if char_deque.popleft() != char_deque.pop():
                return False
                
        return True
