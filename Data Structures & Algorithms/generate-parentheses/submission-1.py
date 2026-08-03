class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(currStr: List[str], opened: int, closed: int) -> None:
            if max(opened, closed) > n or closed > opened:
                return

            if opened == closed == n:
                result.append("".join(currStr))
                return

            currStr.append("(")
            dfs(currStr, opened + 1, closed)
            currStr.pop()
            currStr.append(")")
            dfs(currStr, opened, closed + 1)
            currStr.pop()

        dfs([], 0, 0)
        return result

        