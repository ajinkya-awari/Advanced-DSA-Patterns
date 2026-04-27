import re
from typing import List, Dict, Final

class ExpressionEvaluator:
    """
    Standard Infix to RPN Evaluator using two-stack Shunting-yard algorithm.
    """
    
    _PRECEDENCE: Final[Dict[str, int]] = {'+': 1, '-': 1, '*': 2, '/': 2}

    @classmethod
    def evaluate(cls, expression: str) -> float:
        """
        Parses and evaluates a mathematical expression.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()]', expression)
        postfix = cls._to_postfix(tokens)
        return cls._evaluate_postfix(postfix)

    @classmethod
    def _to_postfix(cls, tokens: List[str]) -> List[str]:
        output: List[str] = []
        operators: List[str] = []

        for token in tokens:
            if re.match(r'\d+', token):
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop() # Remove '('
            else:
                while operators and operators[-1] != '(' and \
                      cls._PRECEDENCE.get(operators[-1], 0) >= cls._PRECEDENCE.get(token, 0):
                    output.append(operators.pop())
                operators.append(token)
        
        while operators:
            output.append(operators.pop())
        return output

    @classmethod
    def _evaluate_postfix(cls, postfix: List[str]) -> float:
        stack: List[float] = []
        for token in postfix:
            if re.match(r'\d+', token):
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(a / b)
        return stack[0]
