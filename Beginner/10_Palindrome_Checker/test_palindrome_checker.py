import pytest
from palindrome_checker import PalindromeChecker

@pytest.mark.parametrize("test_input, expected", [
    ("racecar", True),
    ("A man, a plan, a canal: Panama", True),
    ("No 'x' in Nixon", True),
    ("12321", True),
    ("hello", False),
    ("Python", False),
    ("ab", False),
    ("", True),
    ("a", True),
    (".,", True), # Becomes empty string
    (None, False)
])
def test_palindrome_logic(test_input, expected):
    """Verify various string patterns for palindrome symmetry."""
    assert PalindromeChecker.is_palindrome(test_input) == expected

def test_case_insensitivity():
    """Verify that 'Madam' is treated as 'madam'."""
    assert PalindromeChecker.is_palindrome("Madam") is True

def test_alphanumeric_mixing():
    """Verify that numbers and letters are handled correctly."""
    assert PalindromeChecker.is_palindrome("R33r") is True
    assert PalindromeChecker.is_palindrome("123a321") is True
