import pytest
from leaderboard_ranking_system import Leaderboard, PlayerRecord

@pytest.fixture
def leaderboard():
    lb = Leaderboard()
    lb.update_score("player_1", 100)
    lb.update_score("player_2", 200)
    lb.update_score("player_3", 150)
    return lb

def test_initial_ranking(leaderboard):
    """Verify that players are sorted descending by score."""
    top_3 = leaderboard.get_top_k(3)
    assert top_3[0].player_id == "player_2" # 200
    assert top_3[1].player_id == "player_3" # 150
    assert top_3[2].player_id == "player_1" # 100

def test_score_update_promotion(leaderboard):
    """Verify player moves up when score increases."""
    leaderboard.update_score("player_1", 250)
    assert leaderboard.get_rank("player_1") == 1
    assert leaderboard.get_top_k(1)[0].player_id == "player_1"

def test_score_update_demotion(leaderboard):
    """Verify player moves down when score decreases."""
    leaderboard.update_score("player_2", 50)
    assert leaderboard.get_rank("player_2") == 3

def test_tie_breaking_logic():
    """Verify deterministic ranking for identical scores (ID ascending)."""
    lb = Leaderboard()
    lb.update_score("z_player", 100)
    lb.update_score("a_player", 100)
    
    top_2 = lb.get_top_k(2)
    assert top_2[0].player_id == "a_player"
    assert top_2[1].player_id == "z_player"

def test_top_k_bounds(leaderboard):
    """Verify k values larger than size or zero."""
    assert len(leaderboard.get_top_k(10)) == 3
    assert len(leaderboard.get_top_k(0)) == 0

def test_non_existent_player(leaderboard):
    """Verify rank retrieval for missing players."""
    assert leaderboard.get_rank("ghost") is None

def test_bulk_updates():
    """Stress test the sorted invariant with multiple updates."""
    lb = Leaderboard()
    for i in range(100):
        lb.update_score(f"p{i}", i)
    
    assert lb.get_rank("p99") == 1
    assert lb.get_rank("p0") == 100
    assert lb.total_players == 100
