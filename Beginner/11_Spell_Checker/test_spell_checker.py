import pytest
from spell_checker import SpellChecker

@pytest.fixture
def checker():
    return SpellChecker()

def test_basic_spell_check(checker):
    """Verify standard insertion and lookup."""
    checker.add_word("Enterprise")
    checker.add_word("Software")
    assert checker.check_word("enterprise") is True
    assert checker.check_word("software") is True
    assert checker.check_word("bug") is False

def test_collision_handling(checker):
    """Verify chaining by checking words that might hash to similar buckets."""
    words = ["apple", "apply", "ample", "angle", "ankle"]
    for w in words:
        checker.add_word(w)
    
    for w in words:
        assert checker.check_word(w) is True
    assert checker.dictionary_size == 5

def test_dynamic_rehashing(checker):
    """Verify that the table resizes when load factor is exceeded."""
    initial_cap = checker.current_capacity
    # Fill up to exceed threshold (101 * 0.75 = 75)
    for i in range(80):
        checker.add_word(f"word_{i}")
    
    assert checker.current_capacity > initial_cap
    assert checker.check_word("word_79") is True
    assert checker.check_word("word_0") is True

def test_case_and_whitespace(checker):
    """Verify normalization layer."""
    checker.add_word("  Python  ")
    assert checker.check_word("PYTHON") is True
    assert checker.check_word("python") is True

def test_empty_inputs(checker):
    """Verify robustness against invalid strings."""
    checker.add_word("")
    assert checker.dictionary_size == 0
    assert checker.check_word("") is False
