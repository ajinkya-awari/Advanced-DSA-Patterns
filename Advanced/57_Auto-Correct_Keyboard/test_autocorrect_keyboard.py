import pytest
from autocorrect_keyboard import AutoCorrect

def test_autocorrect():
    ac = AutoCorrect(["apple", "apply", "ball", "bat"])
    assert ac.get_correction("aple") == "apple"
    assert ac.get_correction("bal") == "ball"
