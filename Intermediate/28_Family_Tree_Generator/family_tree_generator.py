from typing import Optional, List, Final
from dataclasses import dataclass

@dataclass
class Person:
    """Represents an individual in the family tree."""
    name: str
    generation: int

class FamilyNode:
    """Node in the family tree."""
    def __init__(self, person: Person):
        self.person: Person = person
        self.left_child: Optional['FamilyNode'] = None
        self.right_child: Optional['FamilyNode'] = None

class FamilyTree:
    """
    Enterprise-grade Family Tree Generator using Binary Tree structures.
    """

    def __init__(self, root_name: str):
        self._root: FamilyNode = FamilyNode(Person(root_name, 0))

    def _find_node(self, current: Optional[FamilyNode], name: str) -> Optional[FamilyNode]:
        """Recursive DFS to find a person by name."""
        if not current:
            return None
        if current.person.name.lower() == name.lower():
            return current
        
        left = self._find_node(current.left_child, name)
        if left: return left
        return self._find_node(current.right_child, name)

    def add_child(self, parent_name: str, child_name: str, side: str = "left") -> bool:
        """
        Adds a child to a specific parent.
        Time Complexity: O(N) for search.
        """
        parent = self._find_node(self._root, parent_name)
        if not parent:
            raise KeyError(f"Parent {parent_name} not found.")

        new_person = Person(child_name, parent.person.generation + 1)
        new_node = FamilyNode(new_person)

        if side.lower() == "left":
            if parent.left_child: return False
            parent.left_child = new_node
        else:
            if parent.right_child: return False
            parent.right_child = new_node
        return True

    def get_lineage(self, name: str) -> List[str]:
        """
        Returns the path from root to the specified person.
        Time Complexity: O(N).
        """
        path: List[str] = []
        self._find_path(self._root, name.lower(), path)
        return path

    def _find_path(self, current: Optional[FamilyNode], name: str, path: List[str]) -> bool:
        if not current:
            return False
        
        path.append(current.person.name)
        if current.person.name.lower() == name:
            return True
        
        if self._find_path(current.left_child, name, path) or \
           self._find_path(current.right_child, name, path):
            return True
        
        path.pop()
        return False
