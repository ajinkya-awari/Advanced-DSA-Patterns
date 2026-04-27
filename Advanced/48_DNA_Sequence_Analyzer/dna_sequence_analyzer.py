from typing import List

class DNAAnalyzer:
    """Genomic analyzer using Dynamic Programming for LCS."""
    @staticmethod
    def longest_common_subsequence(seq1: str, seq2: str) -> str:
        """Time: O(N*M), Space: O(N*M)"""
        n, m = len(seq1), len(seq2)
        dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if seq1[i-1] == seq2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + seq1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
        return dp[n][m]
