import pytest
from dictionary_app import DictionaryApp

@pytest.fixture
def dictionary():
    app = DictionaryApp()
    app.add_word("Algorithm", "A set of rules for solving problems.", "Noun")
    app.add_word("Almanac", "An annual calendar containing data.", "Noun")
    app.add_word("Apple", "A round fruit with red or green skin.", "Noun")
    return app

def test_exact_lookup(dictionary):
    """Verify O(1) definition retrieval."""
    entry = dictionary.get_definition("algorithm")
    assert entry is not None
    assert "set of rules" in entry.definition
    assert entry.part_of_speech == "Noun"

def test_prefix_suggestions(dictionary):
    """Verify Trie-based word discovery."""
    suggestions = dictionary.suggest_words("al")
    assert sorted(suggestions) == ["algorithm", "almanac"]
    
    suggestions_a = dictionary.suggest_words("a")
    assert len(suggestions_a) == 3

def test_case_insensitivity(dictionary):
    """Verify that inputs are normalized."""
    assert dictionary.get_definition("APPLE") is not None
    assert "apple" in dictionary.suggest_words("Ap")

def test_delete_word(dictionary):
    """Verify that removal updates both structures."""
    assert dictionary.delete_word("apple") is True
    assert dictionary.get_definition("apple") is None
    assert "apple" not in dictionary.suggest_words("a")
    assert dictionary.vocabulary_size == 2

def test_invalid_inputs(dictionary):
    """Verify defensive checks."""
    with pytest.raises(ValueError):
        dictionary.add_word("", "", "")
    
    assert dictionary.suggest_words("xyz") == []
    assert dictionary.get_definition("ghost") is None

def test_bulk_capacity():
    """Verify consistency with larger sets."""
    app = DictionaryApp()
    for i in range(100):
        app.add_word(f"word{i}", f"def{i}", "test")
    
    assert app.vocabulary_size == 100
    assert len(app.suggest_words("word1")) == 11 # word1, word10-word19
