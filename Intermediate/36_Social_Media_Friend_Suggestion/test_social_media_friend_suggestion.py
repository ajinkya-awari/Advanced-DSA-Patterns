import pytest
from social_media_friend_suggestion import SocialGraph

def test_friend_suggestions():
    sg = SocialGraph()
    # Alice -> Bob, Alice -> Charlie
    # Bob -> Dave, Charlie -> Dave
    # Dave should be recommended to Alice with 2 mutual friends
    sg.add_friendship("Alice", "Bob")
    sg.add_friendship("Alice", "Charlie")
    sg.add_friendship("Bob", "Dave")
    sg.add_friendship("Charlie", "Dave")
    
    suggestions = sg.suggest_friends("Alice")
    assert suggestions[0] == ("Dave", 2)

def test_no_suggestions():
    sg = SocialGraph()
    sg.add_friendship("Alice", "Bob")
    assert sg.suggest_friends("Alice") == []
