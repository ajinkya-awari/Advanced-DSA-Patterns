import pytest
from simple_text_editor import SimpleTextEditor

@pytest.fixture
def editor():
    return SimpleTextEditor()

def test_append_operation(editor):
    """Verify text is appended correctly."""
    editor.append("abc")
    assert editor.text == "abc"
    editor.append("def")
    assert editor.text == "abcdef"

def test_delete_operation(editor):
    """Verify characters are removed from the end."""
    editor.append("abcde")
    editor.delete(2)
    assert editor.text == "abc"
    
    # Delete more than available
    editor.delete(10)
    assert editor.text == ""

def test_get_char_indexing(editor):
    """Verify 1-based character retrieval."""
    editor.append("abcdef")
    assert editor.get_char(1) == "a"
    assert editor.get_char(6) == "f"
    
    with pytest.raises(IndexError):
        editor.get_char(0)
    with pytest.raises(IndexError):
        editor.get_char(7)

def test_undo_functionality(editor):
    """Verify that multiple operations can be undone."""
    editor.append("abc")
    editor.append("def") # "abcdef"
    editor.delete(2)     # "abcd"
    
    assert editor.text == "abcd"
    
    # First undo reverts the delete
    assert editor.undo() is True
    assert editor.text == "abcdef"
    
    # Second undo reverts the second append
    assert editor.undo() is True
    assert editor.text == "abc"
    
    # Third undo reverts the first append
    assert editor.undo() is True
    assert editor.text == ""
    
    # No more history
    assert editor.undo() is False

def test_empty_operations(editor):
    """Verify robustness against empty inputs."""
    editor.append("")
    assert editor.text == ""
    assert editor.undo() is False # No state change recorded for empty append

def test_complex_sequence(editor):
    """HackerRank typical test case."""
    editor.append("abc")
    editor.delete(3)
    editor.append("xy")
    assert editor.get_char(2) == "y"
    editor.undo()
    assert editor.text == ""
