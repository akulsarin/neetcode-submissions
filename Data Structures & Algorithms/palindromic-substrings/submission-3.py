class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        num_palindromes = 0

        for i in range(N):
            # Odd-length palindromes
            l = r = i
            while l >= 0 and r < N and s[l] == s[r]:
                num_palindromes += 1
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                num_palindromes += 1
                l -= 1
                r += 1
        
        return num_palindromes