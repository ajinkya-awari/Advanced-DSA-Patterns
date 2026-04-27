import pytest
from compiler_design import CompilerParser

def test_ast_construction():
    # 3 4 + (Postfix for 3+4)
    tokens = ["3", "4", "+"]
    root = CompilerParser.build_ast(tokens)
    assert root.value == "+"
    assert root.left.value == "3"
    assert root.right.value == "4"
