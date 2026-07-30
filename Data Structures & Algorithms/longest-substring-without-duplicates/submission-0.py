class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        currMax = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            r += 1
            currMax = max(currMax, r - l)

        return currMax