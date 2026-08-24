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

        def backtrack(start: int, curr: List[str]):
            if start == N:
                res.append(curr.copy())
                return

            for end in range(start, N):
                if dp[start][end]:
                    curr.append(s[start : end + 1])
                    backtrack(end + 1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res