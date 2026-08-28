class Solution:
    def evaluate(self, second_op: str, first_op: str, operator: str) -> str:
        if operator == "+":
            return str(int(first_op) + int(second_op))
        elif operator == "-":
            return str(int(first_op) - int(second_op))
        elif operator == "*":
            return str(int(first_op) * int(second_op))
        else:
            return str(int(int(first_op) / int(second_op)))


    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                stack.append(self.evaluate(stack.pop(), stack.pop(), token))
            else:
                stack.append(token)
        return int(stack[0])