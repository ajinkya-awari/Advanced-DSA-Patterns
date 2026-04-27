from typing import List, Dict, Set, Optional, Tuple, Final
from dataclasses import dataclass, field
from collections import Counter

@dataclass(frozen=True)
class Movie:
    """Immutable entity representing a movie."""
    movie_id: str
    title: str
    genre: str

class MovieRecommendationSystem:
    """
    Enterprise-grade Recommendation Engine using a Bipartite Graph.
    
    Attributes:
        _movies (Dict[str, Movie]): Registry of movie metadata.
        _user_to_movies (Dict[str, Set[str]]): Adjacency list: User -> Liked Movies.
        _movie_to_users (Dict[str, Set[str]]): Adjacency list: Movie -> Users who liked it.
    """

    def __init__(self):
        self._movies: Dict[str, Movie] = {}
        self._user_to_movies: Dict[str, Set[str]] = {}
        self._movie_to_users: Dict[str, Set[str]] = {}

    def add_movie(self, movie_id: str, title: str, genre: str) -> None:
        """Registers a movie in the system."""
        if movie_id in self._movies:
            raise ValueError(f"Movie ID {movie_id} already exists.")
        self._movies[movie_id] = Movie(movie_id, title, genre)
        self._movie_to_users[movie_id] = set()

    def add_user_preference(self, user_id: str, movie_id: str) -> None:
        """
        Creates an edge between a user and a movie (Like interaction).
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if movie_id not in self._movies:
            raise KeyError(f"Movie {movie_id} not found.")

        if user_id not in self._user_to_movies:
            self._user_to_movies[user_id] = set()
        
        self._user_to_movies[user_id].add(movie_id)
        self._movie_to_users[movie_id].add(user_id)

    def get_recommendations(self, user_id: str, limit: int = 5) -> List[Tuple[Movie, int]]:
        """
        Generates recommendations based on shared user preferences.
        
        Time Complexity: O(U * M) where U is similar users and M is their movie sets.
        Space Complexity: O(M) for the candidate aggregation.
        """
        if user_id not in self._user_to_movies:
            return []

        target_liked_movies = self._user_to_movies[user_id]
        candidate_scores: Counter = Counter()

        # Step 2: Find unique Peer Users (who shared at least one movie with target)
        peers: Set[str] = set()
        for movie_id in target_liked_movies:
            movie_peers = self._movie_to_users.get(movie_id, set())
            peers.update(movie_peers)
        
        # Remove target user from peer set
        peers.discard(user_id)

        # Step 3: Collect all movies liked by those Peers that the target hasn't seen
        for peer_id in peers:
            peer_movies = self._user_to_movies.get(peer_id, set())
            for peer_movie_id in peer_movies:
                if peer_movie_id not in target_liked_movies:
                    candidate_scores[peer_movie_id] += 1

        # Step 4: Sort and resolve metadata
        top_candidates = candidate_scores.most_common(limit)
        return [(self._movies[m_id], score) for m_id, score in top_candidates]

    def get_movie_details(self, movie_id: str) -> Optional[Movie]:
        return self._movies.get(movie_id)

    @property
    def movie_count(self) -> int:
        return len(self._movies)
