import pytest
from autocomplete_search_engine import AutocompleteEngine

@pytest.fixture
def engine():
    e = AutocompleteEngine()
    e.bulk_insert(["apple", "app", "apply", "ball", "bat", "batman", "bath"])
    return e

def test_exact_prefix_match(engine):
    """Verify that a shared prefix returns all valid children."""
    results = engine.search_prefix("app")
    assert sorted(results) == ["app", "apple", "apply"]

def test_unique_prefix(engine):
    """Verify that unique branches are isolated."""
    results = engine.search_prefix("ba")
    assert sorted(results) == ["ball", "bat", "bath", "batman"]

def test_no_match(engine):
    """Verify empty list for non-existent prefixes."""
    assert engine.search_prefix("cat") == []

def test_case_insensitivity(engine):
    """Verify system handles mixed casing gracefully."""
    results = engine.search_prefix("APP")
    assert sorted(results) == ["app", "apple", "apply"]

def test_empty_inputs(engine):
    """Verify robustness against null/empty strings."""
    assert engine.search_prefix("") == []
    engine.insert("") # Should not crash

def test_large_dataset_simulation():
    """Verify performance and accuracy with 1000+ words."""
    large_engine = AutocompleteEngine()
    words = [f"word_{i}" for i in range(1500)]
    large_engine.bulk_insert(words)
    
    # Search for a specific prefix
    results = large_engine.search_prefix("word_100")
    # Should find "word_100", "word_1000", "word_1001"..."word_1009"
    assert len(results) == 11
    assert "word_1009" in results
