class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counts = defaultdict(int)
        l = r = 0
        while r < k:
            counts[blocks[r]] += 1
            r += 1

        r -= 1
        res = counts["W"]
        while r + 1 < len(blocks):
            print(l, r, res)
            counts[blocks[l]] -= 1
            l += 1
            r += 1
            counts[blocks[r]] += 1
            res = min(res, counts["W"])
        
        return res