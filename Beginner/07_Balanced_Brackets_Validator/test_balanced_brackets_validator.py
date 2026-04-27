import pytest
from balanced_brackets_validator import BalancedBracketsValidator

@pytest.mark.parametrize("test_input, expected", [
    ("()", True),
    ("()[]{}", True),
    ("( [ { } ] )", True),
    ("((()))", True),
    ("", True),
    ("abc(123)", True),
    ("(", False),
    (")", False),
    ("([)]", False),
    ("((()", False),
    ("}{", False),
    ("( [ ) ]", False)
])
def test_bracket_validation(test_input, expected):
    """Verify various combinations of balanced and unbalanced inputs."""
    assert BalancedBracketsValidator.is_balanced(test_input) == expected

def test_complex_nesting():
    """Verify deep and complex nesting patterns."""
    complex_input = "{[()()]{}[()]}"
    assert BalancedBracketsValidator.is_balanced(complex_input) is True

def test_mismatched_types():
    """Verify that mismatching bracket types returns False."""
    assert BalancedBracketsValidator.is_balanced("{[}]") is False

def test_interspersed_content():
    """Verify that non-bracket characters do not interfere with validation."""
    interspersed = "def func(a: list[int]) -> dict{str: int}: return {}"
    assert BalancedBracketsValidator.is_balanced(interspersed) is True
