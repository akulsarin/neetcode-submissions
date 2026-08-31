class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_freqs = defaultdict(int)
        max_freq = 0
        l = 0
        result = 0

        for r, char in enumerate(s):
            window_freqs[char] += 1
            max_freq = max(max_freq, window_freqs[char])
            
            if r - l + 1 - max_freq > k:
                window_freqs[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result