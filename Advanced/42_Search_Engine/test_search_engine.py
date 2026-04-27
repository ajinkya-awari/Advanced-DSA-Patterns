import pytest
from search_engine import SearchEngine

def test_search_ranking():
    engine = SearchEngine()
    engine.index_document("D1", "Python Guide", "python python python is great")
    engine.index_document("D2", "Java Basics", "java is also used")
    engine.index_document("D3", "Mixed Tech", "python and java together")
    
    results = engine.search("python")
    # D1 has 3 occurrences, D3 has 1. D1 should be first.
    assert results[0][0] == "Python Guide"
    assert results[0][1] == 3
    assert results[1][0] == "Mixed Tech"

def test_search_no_results():
    engine = SearchEngine()
    engine.index_document("D1", "Title", "content")
    assert engine.search("missing") == []
