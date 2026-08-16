class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wCounts = 0
        for i in range(k):
            if blocks[i] == "W":
                wCounts += 1

        res = wCounts
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                wCounts += 1
            if blocks[i - k] == "W":
                wCounts -= 1
            res = min(res, wCounts)
        
        return res