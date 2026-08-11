class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        endIndices = {}
        for i, c in enumerate(s):
            endIndices[c] = i


        start, end = 0, 0
        res = []
        for i, c in enumerate(s):
            end = max(end, endIndices[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
        