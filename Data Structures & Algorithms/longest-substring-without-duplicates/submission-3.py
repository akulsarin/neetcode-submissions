class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N <= 1:
            return N

        l, r = 0, 1
        currMax = 1
        uniqueChars = {s[l]}

        while r < N:
            if s[r] in uniqueChars:
                while s[r] in uniqueChars:
                    uniqueChars.remove(s[l])
                    l += 1
            
            uniqueChars.add(s[r])
            currMax = max(currMax, r - l + 1)
            r += 1

        return currMax
        