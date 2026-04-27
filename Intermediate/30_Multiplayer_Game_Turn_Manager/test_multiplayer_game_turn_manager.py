import pytest
from multiplayer_game_turn_manager import TurnManager

@pytest.fixture
def manager():
    return TurnManager(["Alice", "Bob", "Charlie"])

def test_rotation(manager):
    assert manager.next_turn() == "Alice"
    assert manager.next_turn() == "Bob"
    assert manager.next_turn() == "Charlie"
    assert manager.next_turn() == "Alice" # Circular

def test_add_remove(manager):
    manager.add_player("Dave")
    assert manager.player_count == 4
    manager.remove_player("Bob")
    assert manager.player_count == 3
    # Check rotation without Bob
    manager.next_turn() # Alice
    assert manager.next_turn() == "Charlie"
