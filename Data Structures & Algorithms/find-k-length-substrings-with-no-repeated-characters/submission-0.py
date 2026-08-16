class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        N = len(s)
        if k > N:
            return 0

        windowChars = set()
        count = 0
        l = 0

        for r in range(N):
            while s[r] in windowChars:
                windowChars.remove(s[l])
                l += 1
            
            windowChars.add(s[r])

            if r - l + 1 == k:
                count += 1
                windowChars.remove(s[l])
                l += 1

        return count