from typing import List, Final

class TextEditor:
    """
    A production-grade text editor simulation with Undo/Redo capabilities.
    
    Attributes:
        _content (str): Current text content.
        _undo_stack (List[str]): LIFO stack for history.
        _redo_stack (List[str]): LIFO stack for reverted actions.
    """

    def __init__(self, initial_text: str = ""):
        self._content: str = initial_text
        self._undo_stack: List[str] = []
        self._redo_stack: List[str] = []

    def write(self, text: str) -> None:
        """
        Appends text to the editor and updates history.
        
        Time Complexity: O(N) where N is the length of the string (snapshotting).
        Space Complexity: O(N)
        """
        # Save current state to undo stack
        self._undo_stack.append(self._content)
        # Apply change
        self._content += text
        # New operations invalidate redo history
        self._redo_stack.clear()

    def undo(self) -> bool:
        """
        Reverts the last operation.
        
        Time Complexity: O(1) (stack operations)
        Space Complexity: O(1)
        """
        if not self._undo_stack:
            return False

        # Move current state to redo stack
        self._redo_stack.append(self._content)
        # Restore state from undo stack
        self._content = self._undo_stack.pop()
        return True

    def redo(self) -> bool:
        """
        Restores the last undone operation.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._redo_stack:
            return False

        # Move current state to undo stack
        self._undo_stack.append(self._content)
        # Restore state from redo stack
        self._content = self._redo_stack.pop()
        return True

    @property
    def content(self) -> str:
        """Returns the current document content."""
        return self._content

    def __repr__(self) -> str:
        return f"TextEditor(content='{self._content}')"
