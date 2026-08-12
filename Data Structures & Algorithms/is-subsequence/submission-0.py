class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        M, N = len(s), len(t)
        i = j = 0
        while i < M and j < N:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == M