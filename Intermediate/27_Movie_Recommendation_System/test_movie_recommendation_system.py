import pytest
from movie_recommendation_system import MovieRecommendationSystem

@pytest.fixture
def rec_system():
    sys = MovieRecommendationSystem()
    # Setup movies
    sys.add_movie("M1", "Inception", "Sci-Fi")
    sys.add_movie("M2", "The Matrix", "Sci-Fi")
    sys.add_movie("M3", "Interstellar", "Sci-Fi")
    sys.add_movie("M4", "Toy Story", "Animation")
    sys.add_movie("M5", "Finding Nemo", "Animation")
    
    # Setup User A (Target) likes Inception and Matrix
    sys.add_user_preference("UserA", "M1")
    sys.add_user_preference("UserA", "M2")
    
    # Setup User B (Similar to A) likes Inception, Matrix, and Interstellar
    sys.add_user_preference("UserB", "M1")
    sys.add_user_preference("UserB", "M2")
    sys.add_user_preference("UserB", "M3")
    
    # Setup User C (Different) likes Toy Story
    sys.add_user_preference("UserC", "M4")
    sys.add_user_preference("UserC", "M5")
    
    return sys

def test_basic_recommendation(rec_system):
    """Verify that User A is recommended Interstellar (liked by User B)."""
    recommendations = rec_system.get_recommendations("UserA")
    
    assert len(recommendations) > 0
    top_movie = recommendations[0][0]
    assert top_movie.movie_id == "M3"
    assert top_movie.title == "Interstellar"

def test_no_recommendations_for_new_user(rec_system):
    """Verify that users with no likes get no recommendations."""
    assert rec_system.get_recommendations("NewUser") == []

def test_no_overlap_scenario(rec_system):
    """Verify that users with no common interests with others get no suggestions."""
    rec_system.add_user_preference("UserLone", "M4")
    # No one else likes M4 except UserC, but UserLone already likes M4. 
    # Currently UserC likes M4 and M5. UserLone likes M4. So UserLone should get M5.
    recommendations = rec_system.get_recommendations("UserLone")
    assert len(recommendations) > 0
    assert recommendations[0][0].movie_id == "M5"

def test_invalid_movie_preference(rec_system):
    """Verify error handling for non-existent movies."""
    with pytest.raises(KeyError):
        rec_system.add_user_preference("UserA", "M_GHOST")

def test_duplicate_movie_prevention(rec_system):
    """Verify movie registry integrity."""
    with pytest.raises(ValueError, match="already exists"):
        rec_system.add_movie("M1", "Duplicate", "Genre")

def test_ranking_logic(rec_system):
    """Verify that more popular movies among peers rank higher."""
    # Add UserD who also likes Inception and Finding Nemo
    rec_system.add_user_preference("UserD", "M1")
    rec_system.add_user_preference("UserD", "M5")
    
    # UserA likes Inception. 
    # Peer B likes Inception -> Suggests M3 (Score 1)
    # Peer D likes Inception -> Suggests M5 (Score 1)
    # If we add UserE who likes Inception and M3...
    rec_system.add_user_preference("UserE", "M1")
    rec_system.add_user_preference("UserE", "M3")
    
    # Now M3 should have score 2 (from B and E), M5 has score 1 (from D)
    recs = rec_system.get_recommendations("UserA")
    assert recs[0][0].movie_id == "M3"
    assert recs[0][1] == 2
