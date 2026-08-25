class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_chars = defaultdict(int)
        maxFreq = 0
        ans = 0
        l = 0

        for r in range(len(s)):
            window_chars[s[r]] += 1
            maxFreq = max(maxFreq, window_chars[s[r]])

            if (r - l + 1) - maxFreq > k:
                window_chars[s[l]] -= 1
                if window_chars[s[l]] == 0:
                    del window_chars[s[l]]
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans