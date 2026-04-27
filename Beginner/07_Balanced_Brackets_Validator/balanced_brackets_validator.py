from typing import Dict, List, Final

class BalancedBracketsValidator:
    """
    Enterprise-grade validator for bracket balance and nesting integrity.
    
    Supported brackets: (), [], {}
    """

    # Mapping of closing brackets to their respective opening brackets
    _BRACKET_MAP: Final[Dict[str, str]] = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    _OPENING_BRACKETS: Final[set] = set(_BRACKET_MAP.values())

    @classmethod
    def is_balanced(cls, input_string: str) -> bool:
        """
        Validates if the brackets in the string are balanced and correctly nested.
        
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) in the worst case (e.g., all opening brackets).
        """
        if not input_string:
            return True

        stack: List[str] = []

        for char in input_string:
            if char in cls._OPENING_BRACKETS:
                stack.append(char)
            elif char in cls._BRACKET_MAP:
                # If stack is empty or top of stack doesn't match
                if not stack or stack.pop() != cls._BRACKET_MAP[char]:
                    return False
            else:
                # Ignore non-bracket characters
                continue

        # Valid only if no opening brackets remain
        return len(stack) == 0
