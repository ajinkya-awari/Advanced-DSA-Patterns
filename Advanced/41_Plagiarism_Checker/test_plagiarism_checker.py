import pytest
from plagiarism_checker import PlagiarismChecker

def test_plagiarism_detection():
    checker = PlagiarismChecker(window_size=5)
    doc_a = "The quick brown fox jumps over the lazy dog"
    doc_b = "The quick brown fox sleeps all day"
    
    similarity = checker.check_similarity(doc_a, doc_b)
    assert similarity > 0.3 # High overlap in the first half

def test_no_plagiarism():
    checker = PlagiarismChecker(window_size=5)
    doc_a = "Python is a programming language"
    doc_b = "SpaceX builds rockets"
    assert checker.check_similarity(doc_a, doc_b) == 0.0

def test_identical_docs():
    checker = PlagiarismChecker(window_size=5)
    doc = "Repeatable text string"
    assert checker.check_similarity(doc, doc) == 1.0
