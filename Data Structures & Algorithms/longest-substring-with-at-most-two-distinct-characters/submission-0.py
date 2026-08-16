class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        windowChars = {}
        maxLen = 0
        for r, char in enumerate(s):
            if char in windowChars:
                maxLen = max(maxLen, r - l + 1)
                windowChars[char] += 1
                continue

            while len(windowChars) == 2:
                windowChars[s[l]] -= 1
                if windowChars[s[l]] == 0:
                    del windowChars[s[l]]
                l += 1

            maxLen = max(maxLen, r - l + 1)
            windowChars[char] = 1

        return maxLen