class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        def backtrack(curr: List[str], num_open: int, num_closed: int) -> None:
            if len(curr) == 2 * n:
                parentheses.append("".join(curr))
                return
            
            if num_open < n:
                curr.append("(")
                backtrack(curr, num_open + 1, num_closed)
                curr.pop()

            if num_closed < num_open:
                curr.append(")")
                backtrack(curr, num_open, num_closed + 1)
                curr.pop()
        
        backtrack([], 0, 0)
        return parentheses