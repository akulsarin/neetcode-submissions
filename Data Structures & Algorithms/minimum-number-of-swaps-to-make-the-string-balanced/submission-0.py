class Solution:
    def minSwaps(self, s: str) -> int:
        count = unmatched = 0
        for c in s:
            if c == "]":
                count += 1
            else:
                count -= 1
            unmatched = max(count, unmatched)
        return (unmatched + 1) // 2

        