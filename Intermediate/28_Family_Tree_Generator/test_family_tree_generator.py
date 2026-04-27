import pytest
from family_tree_generator import FamilyTree

@pytest.fixture
def tree():
    return FamilyTree("Grandpa")

def test_add_and_find(tree):
    tree.add_child("Grandpa", "Dad", "left")
    tree.add_child("Dad", "Me", "left")
    lineage = tree.get_lineage("Me")
    assert lineage == ["Grandpa", "Dad", "Me"]

def test_invalid_parent(tree):
    with pytest.raises(KeyError):
        tree.add_child("Ghost", "Child")

def test_occupied_side(tree):
    tree.add_child("Grandpa", "Child1", "left")
    assert tree.add_child("Grandpa", "Child2", "left") is False
