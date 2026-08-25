class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_chars = [0] * 26
        max_freq = 0
        max_len = 0
        l = 0

        for r in range(len(s)):
            r_idx = ord(s[r]) - ord('A')
            window_chars[r_idx] += 1
            max_freq = max(max_freq, window_chars[r_idx])

            if (r - l + 1) - max_freq > k:
                l_idx = ord(s[l]) - ord('A')
                window_chars[l_idx] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len