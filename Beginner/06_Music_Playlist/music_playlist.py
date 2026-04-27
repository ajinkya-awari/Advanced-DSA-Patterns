from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Song:
    """Represents a music track."""
    title: str
    artist: str

class SongNode:
    """A node in the Circular Linked List."""
    def __init__(self, song: Song):
        self.song: Song = song
        self.next: Optional['SongNode'] = None

class MusicPlaylist:
    """
    Production-grade Music Playlist using a Singly Circular Linked List.
    
    Attributes:
        _head (Optional[SongNode]): The first song in the playlist.
        _tail (Optional[SongNode]): The last song, pointing back to head.
        _current (Optional[SongNode]): The currently playing song.
        _size (int): Total song count.
    """

    def __init__(self):
        self._head: Optional[SongNode] = None
        self._tail: Optional[SongNode] = None
        self._current: Optional[SongNode] = None
        self._size: int = 0

    def add_song(self, title: str, artist: str) -> None:
        """
        Appends a song to the playlist.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_song = Song(title, artist)
        new_node = SongNode(new_song)

        if not self._head:
            self._head = new_node
            self._tail = new_node
            new_node.next = self._head
            self._current = self._head
        else:
            new_node.next = self._head
            self._tail.next = new_node
            self._tail = new_node
        
        self._size += 1

    def play_next(self) -> Optional[Song]:
        """
        Advances to the next song in the loop.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._current:
            return None
        
        self._current = self._current.next
        return self._current.song

    def remove_song(self, title: str) -> bool:
        """
        Removes a song by title and repairs circular links.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not self._head:
            return False

        current = self._head
        prev = self._tail
        
        for _ in range(self._size):
            if current.song.title.lower() == title.lower():
                # If only one node exists
                if self._size == 1:
                    self._head = self._tail = self._current = None
                else:
                    prev.next = current.next
                    if current == self._head:
                        self._head = current.next
                    if current == self._tail:
                        self._tail = prev
                    if current == self._current:
                        self._current = current.next
                
                self._size -= 1
                return True
            
            prev = current
            current = current.next
            
        return False

    @property
    def current_track(self) -> Optional[Song]:
        return self._current.song if self._current else None

    @property
    def size(self) -> int:
        return self._size
