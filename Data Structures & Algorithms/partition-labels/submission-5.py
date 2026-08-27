class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        last_indices = {c: i for i, c in enumerate(s)}

        l, r = 0, last_indices[s[0]]
        i = 0
        partitions = []
        while i < N:
            r = max(r, last_indices[s[i]])
            if i == r:
                partitions.append(r - l + 1)
                l = r + 1
            i += 1
        return partitions