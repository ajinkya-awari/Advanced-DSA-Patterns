import pytest
from browser_history_manager import BrowserHistoryManager

@pytest.fixture
def browser():
    return BrowserHistoryManager("google.com")

def test_visit_and_current_page(browser):
    """Verify that visiting a page updates the current state."""
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    assert browser.current_url == "stackoverflow.com"

def test_back_navigation(browser):
    """Verify backward traversal through history."""
    browser.visit("a.com")
    browser.visit("b.com")
    browser.visit("c.com")
    
    assert browser.back(1) == "b.com"
    assert browser.back(1) == "a.com"
    assert browser.back(5) == "google.com" # Should stop at homepage

def test_forward_navigation(browser):
    """Verify forward traversal after going back."""
    browser.visit("a.com")
    browser.visit("b.com")
    
    browser.back(2) # Back to google.com
    assert browser.forward(1) == "a.com"
    assert browser.forward(1) == "b.com"
    assert browser.forward(1) == "b.com" # Bounds check

def test_branching_history_truncation(browser):
    """Verify that visiting a new page from history clears the forward path."""
    browser.visit("a.com")
    browser.visit("b.com")
    
    browser.back(1) # At a.com
    browser.visit("c.com") # Forward history "b.com" should be deleted
    
    assert browser.current_url == "c.com"
    assert browser.forward(1) == "c.com" # No b.com anymore
    assert browser.back(1) == "a.com"

def test_single_page_behavior(browser):
    """Verify behavior when no history exists."""
    assert browser.back(1) == "google.com"
    assert browser.forward(1) == "google.com"
