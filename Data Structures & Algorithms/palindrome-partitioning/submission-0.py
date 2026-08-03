class Solution:

    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        result = []

        def dfs(i: int, curr: List[str]):
            if i == N:
                result.append(curr.copy())
                return

            for j in range(i, N):
                if self.isPali(s, i, j):
                    curr.append(s[i : j + 1])
                    dfs(j + 1, curr)
                    curr.pop()

        dfs(0, [])
        return result

    def isPali(self, s: str, l: int, r: int):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True