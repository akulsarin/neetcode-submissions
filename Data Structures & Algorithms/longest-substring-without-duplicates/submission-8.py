class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_indices = defaultdict(lambda: -1)
        longest = 0
        l = 0
        
        for r, char in enumerate(s):
            if last_indices[char] >= l:
                l = last_indices[char] + 1

            last_indices[char] = r
            longest = max(longest, r - l + 1)
        
        return longest