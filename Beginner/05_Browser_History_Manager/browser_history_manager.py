from typing import Optional, Final

class HistoryNode:
    """Represents a single page in the browser history."""
    def __init__(self, url: str):
        self.url: str = url
        self.prev: Optional['HistoryNode'] = None
        self.next: Optional['HistoryNode'] = None

class BrowserHistoryManager:
    """
    Enterprise-grade Browser History Manager using a Doubly Linked List.
    
    Attributes:
        current_page (HistoryNode): The node representing the active URL.
    """

    def __init__(self, homepage: str):
        self._current_page: HistoryNode = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        """
        Visits a new URL, truncating any existing forward history.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_page = HistoryNode(url)
        # Link new page to history
        new_page.prev = self._current_page
        # Truncate forward history (old next is garbage collected)
        self._current_page.next = new_page
        # Advance current pointer
        self._current_page = new_page

    def back(self, steps: int) -> str:
        """
        Navigates back in history by N steps.
        
        Time Complexity: O(Steps)
        Space Complexity: O(1)
        """
        while steps > 0 and self._current_page.prev:
            self._current_page = self._current_page.prev
            steps -= 1
        return self._current_page.url

    def forward(self, steps: int) -> str:
        """
        Navigates forward in history by N steps.
        
        Time Complexity: O(Steps)
        Space Complexity: O(1)
        """
        while steps > 0 and self._current_page.next:
            self._current_page = self._current_page.next
            steps -= 1
        return self._current_page.url

    @property
    def current_url(self) -> str:
        return self._current_page.url
