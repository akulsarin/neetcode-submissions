class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M, N = len(s), len(t)
        if N > M:
            return ""

        targetCounts = Counter(t)
        windowCounts = defaultdict(int)
        matches = 0

        l = 0
        minL = minR = 0
        minLen = float("inf")
        for r, char in enumerate(s):
            windowCounts[char] += 1
            if windowCounts[char] == targetCounts.get(char):
                matches += 1

            while matches == len(targetCounts):
                if r - l + 1 < minLen:
                    minL, minR = l, r
                    minLen = r - l + 1
                lChar = s[l]
                windowCounts[lChar] -= 1
                if windowCounts[lChar] + 1 == targetCounts.get(lChar):
                    matches -= 1
                l += 1
        
        return s[minL : minR + 1] if minLen < float("inf") else ""