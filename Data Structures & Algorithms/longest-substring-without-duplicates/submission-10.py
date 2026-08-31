class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars = {}
        max_len = 0
        l = 0
        
        for r, char in enumerate(s):
            if char in window_chars:
                l = max(l, window_chars[char] + 1)
            window_chars[char] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len