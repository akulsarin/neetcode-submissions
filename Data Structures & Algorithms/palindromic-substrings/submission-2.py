class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0
        for i in range(N):
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count 
        