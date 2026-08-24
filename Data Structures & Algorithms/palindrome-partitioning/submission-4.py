class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        res = []

        # dp[l][r] := whether s[l : r + 1] is a palindrome
        dp = [[False] * N for _ in range(N)]
        for i in range(N):
            # Odd length palindromes
            l = r = i
            while l >= 0 and r < N and s[l] == s[r]:
                dp[l][r] = True
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                dp[l][r] = True
                l -= 1
                r += 1

        def backtrack(l: int, r: int, curr: List[str]):
            if l == N:
                res.append(curr.copy())
            elif r < N:
                if dp[l][r]:
                    curr.append(s[l : r + 1])
                    backtrack(r + 1, r + 1, curr)
                    curr.pop()
                backtrack(l, r + 1, curr)
        
        backtrack(0, 0, [])
        return res