import pytest
from undoredo_feature import TextEditor

@pytest.fixture
def editor():
    return TextEditor(initial_text="Hello")

def test_write_operation(editor):
    """Verify text is appended correctly."""
    editor.write(" World")
    assert editor.content == "Hello World"

def test_undo_functionality(editor):
    """Verify state is reverted correctly."""
    editor.write(" World")
    assert editor.content == "Hello World"
    
    status = editor.undo()
    assert status is True
    assert editor.content == "Hello"

def test_redo_functionality(editor):
    """Verify reverted state is restored correctly."""
    editor.write(" World")
    editor.undo()
    
    status = editor.redo()
    assert status is True
    assert editor.content == "Hello World"

def test_redo_invalidation(editor):
    """Verify that a new write clears the redo stack."""
    editor.write(" A")
    editor.undo()
    assert editor.content == "Hello"
    
    editor.write(" B")
    # Redo should now be impossible
    assert editor.redo() is False
    assert editor.content == "Hello B"

def test_multiple_undo_redo(editor):
    """Verify complex chain of operations."""
    editor.write(" One")   # "Hello One"
    editor.write(" Two")   # "Hello One Two"
    editor.write(" Three") # "Hello One Two Three"
    
    editor.undo()
    editor.undo()
    assert editor.content == "Hello One"
    
    editor.redo()
    assert editor.content == "Hello One Two"

def test_empty_stacks(editor):
    """Verify edge case of performing undo/redo on empty stacks."""
    assert editor.undo() is False  # Empty undo stack
    assert editor.redo() is False  # Empty redo stack
