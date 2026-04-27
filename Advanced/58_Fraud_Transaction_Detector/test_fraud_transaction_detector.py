import pytest
from fraud_transaction_detector import FraudDetector

def test_fraud_cycle():
    fd = FraudDetector()
    fd.add_transaction("A", "B")
    fd.add_transaction("B", "C")
    fd.add_transaction("C", "A") # Cycle
    assert fd.has_cycle() is True

def test_no_fraud():
    fd = FraudDetector()
    fd.add_transaction("A", "B")
    fd.add_transaction("B", "C")
    assert fd.has_cycle() is False
