import pytest
from music_playlist import MusicPlaylist

@pytest.fixture
def playlist():
    p = MusicPlaylist()
    p.add_song("Song A", "Artist 1")
    p.add_song("Song B", "Artist 2")
    p.add_song("Song C", "Artist 3")
    return p

def test_circular_looping(playlist):
    """Verify that playing next from the last song returns to the first."""
    # Current is Song A
    assert playlist.current_track.title == "Song A"
    
    playlist.play_next() # To Song B
    playlist.play_next() # To Song C
    
    # This should loop back to Song A
    next_song = playlist.play_next()
    assert next_song.title == "Song A"
    assert playlist.current_track.title == "Song A"

def test_remove_middle_song(playlist):
    """Verify deletion and link repair."""
    assert playlist.remove_song("Song B") is True
    assert playlist.size == 2
    
    # Check if A points to C now
    assert playlist.current_track.title == "Song A"
    playlist.play_next()
    assert playlist.current_track.title == "Song C"

def test_remove_head_song(playlist):
    """Verify head deletion updates circular tail pointer."""
    playlist.remove_song("Song A")
    assert playlist.current_track.title == "Song B"
    # Ensure loop still works from C to B
    playlist.play_next() # Now at C
    playlist.play_next() # Now back at B
    assert playlist.current_track.title == "Song B"

def test_remove_non_existent(playlist):
    """Verify robustness against missing titles."""
    assert playlist.remove_song("Ghost") is False
    assert playlist.size == 3

def test_empty_playlist_behavior():
    """Verify operations on empty playlist."""
    p = MusicPlaylist()
    assert p.play_next() is None
    assert p.remove_song("Any") is False
