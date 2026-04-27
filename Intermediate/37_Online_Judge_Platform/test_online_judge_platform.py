import pytest
from online_judge_platform import OnlineJudgeLeaderboard

def test_leaderboard_ranking():
    oj = OnlineJudgeLeaderboard()
    oj.update_score("Alice", 50)
    oj.update_score("Bob", 100)
    oj.update_score("Alice", 70) # Alice total 120
    
    top = oj.get_top_k(2)
    assert top[0] == ("Alice", 120)
    assert top[1] == ("Bob", 100)
