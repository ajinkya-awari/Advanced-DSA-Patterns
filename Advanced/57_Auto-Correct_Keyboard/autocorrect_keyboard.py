from typing import List, Dict

class AutoCorrect:
    """Auto-correct logic using Trie and Levenshtein Distance."""
    def __init__(self, dictionary: List[str]):
        self._dict = dictionary

    @staticmethod
    def edit_distance(s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = i
        for j in range(m + 1): dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[n][m]

    def get_correction(self, word: str) -> str:
        word = word.lower()
        return min(self._dict, key=lambda x: self.edit_distance(word, x.lower()))
