import pytest
from online_multiplayer_matchmaking import Matchmaker

def test_matchmaking_brackets():
    m = Matchmaker(["P1", "P2", "P3", "P4"])
    m.union("P1", "P2")
    m.union("P3", "P4")
    assert m.find("P1") == m.find("P2")
    assert m.find("P1") != m.find("P3")
    m.union("P2", "P3")
    assert m.find("P1") == m.find("P4")
