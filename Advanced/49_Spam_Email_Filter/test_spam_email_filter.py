import pytest
from spam_email_filter import SpamFilter

def test_spam_detection():
    sf = SpamFilter(["win", "prize", "free", "money"])
    assert sf.is_spam("You win free money today!") is True
    assert sf.is_spam("Meeting at 5pm in the office.") is False
