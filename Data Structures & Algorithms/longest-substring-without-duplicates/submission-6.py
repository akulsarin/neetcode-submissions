class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in window_chars:
                window_chars.remove(s[l])
                l += 1
            window_chars.add(s[r])
            longest = max(longest, len(window_chars))
        return longest