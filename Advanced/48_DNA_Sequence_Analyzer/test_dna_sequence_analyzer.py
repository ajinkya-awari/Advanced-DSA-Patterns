import pytest
from dna_sequence_analyzer import DNAAnalyzer

def test_lcs_dna():
    analyzer = DNAAnalyzer()
    assert analyzer.longest_common_subsequence("ACCGGTAB", "GXTXAYB") == "GTAB"
    assert analyzer.longest_common_subsequence("AAAA", "AA") == "AA"
