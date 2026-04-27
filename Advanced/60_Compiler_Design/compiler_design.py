from typing import List, Optional

class ASTNode:
    def __init__(self, value: str):
        self.value = value
        self.left: Optional['ASTNode'] = None
        self.right: Optional['ASTNode'] = None

class CompilerParser:
    """Builds an AST from a mathematical expression (Post-fix logic)."""
    @staticmethod
    def build_ast(postfix_tokens: List[str]) -> Optional[ASTNode]:
        stack = []
        for token in postfix_tokens:
            if token.isalnum():
                stack.append(ASTNode(token))
            else:
                node = ASTNode(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack[0] if stack else None
