from typing import List, Final

class SimpleTextEditor:
    """
    Enterprise-grade Text Editor simulation using a state-tracking stack.
    
    Attributes:
        _buffer (str): The current text content of the editor.
        _history (List[str]): LIFO stack storing previous states for undo operations.
    """

    def __init__(self, initial_text: str = ""):
        self._buffer: str = initial_text
        self._history: List[str] = []

    def _save_history(self) -> None:
        """Saves current buffer state to history."""
        self._history.append(self._buffer)

    def append(self, text: str) -> None:
        """
        Appends a string to the end of the buffer.
        
        Time Complexity: O(N + M) where N is buffer length and M is appended text length.
        Space Complexity: O(N) to store the history snapshot.
        """
        if not text:
            return
            
        self._save_history()
        self._buffer += text

    def delete(self, count: int) -> None:
        """
        Removes the last 'count' characters from the buffer.
        
        Time Complexity: O(N) where N is the buffer length.
        Space Complexity: O(N) for history snapshot.
        """
        if count <= 0:
            return
            
        if count > len(self._buffer):
            count = len(self._buffer)
            
        self._save_history()
        self._buffer = self._buffer[:-count]

    def get_char(self, index: int) -> str:
        """
        Returns the character at the specific 1-based index.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # 1-based indexing as per standard editor requirements
        if not (1 <= index <= len(self._buffer)):
            raise IndexError(f"Position {index} is out of bounds.")
            
        return self._buffer[index - 1]

    def undo(self) -> bool:
        """
        Reverts the buffer to the state before the last append or delete.
        
        Time Complexity: O(1) (reference assignment)
        Space Complexity: O(1)
        """
        if not self._history:
            return False
            
        self._buffer = self._history.pop()
        return True

    @property
    def text(self) -> str:
        """Returns current buffer content."""
        return self._buffer

    def __len__(self) -> int:
        return len(self._buffer)
