import pytest
from expression_evaluator import ExpressionEvaluator

def test_basic_arithmetic():
    assert ExpressionEvaluator.evaluate("3 + 4 * 2") == 11.0

def test_parentheses():
    assert ExpressionEvaluator.evaluate("(3 + 4) * 2") == 14.0

def test_complex_expression():
    assert ExpressionEvaluator.evaluate("10 + 2 * (6 / (9 - 7))") == 16.0
