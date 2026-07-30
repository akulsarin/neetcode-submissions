class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        def executeOperator(operator: str, op1: str, op2: str) -> int:
            if operator == "+":
                return op1 + op2
            elif operator == "-":
                return op1 - op2
            elif operator == "*":
                return op1 * op2
            else:
                return int(op1 / op2)

        argStack = []
        for token in tokens:
            if token not in operators:
                argStack.append(int(token))
            else:
                op2 = argStack.pop()
                op1 = argStack.pop()
                result = executeOperator(token, op1, op2)
                argStack.append(result)
        
        return argStack[-1]
            

        