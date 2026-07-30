class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i: int, curr: List[int], res: List[List[int]]):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if i > n:
                return

            for j in range(i, n + 1):
                curr.append(j)
                dfs(j + 1, curr, res)
                curr.pop()

        res = []
        dfs(1, [], res)
        return res
        