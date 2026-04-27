import pytest
from big_data_log_analyzer import LogAnalyzer

def test_log_analysis():
    la = LogAnalyzer()
    la.ingest_log("ERROR: Database connection failed")
    la.ingest_log("ERROR: Database connection failed")
    la.ingest_log("WARN: High memory usage")
    
    assert la.get_frequency("ERROR") == 2
    assert la.get_frequency("WARN") == 1
