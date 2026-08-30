class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        def backtrack(curr: List[str] = [], num_open: int = 0, num_closed: int = 0) -> None:
            if len(curr) == 2 * n:
                parentheses.append("".join(curr))
                return
            
            if num_open < n:
                curr.append("(")
                backtrack(curr, num_open + 1, num_closed)
                curr.pop()

            if num_closed < n and num_closed < num_open:
                curr.append(")")
                backtrack(curr, num_open, num_closed + 1)
                curr.pop()
        
        backtrack()
        return parentheses