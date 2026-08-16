class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        windowChars = {}
        maxLen = 0
        for r, char in enumerate(s):
            if char in windowChars:
                windowChars[char] += 1
            else:
                windowChars[char] = 1

            while len(windowChars) > k:
                windowChars[s[l]] -= 1
                if windowChars[s[l]] == 0:
                    del windowChars[s[l]]
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen
        