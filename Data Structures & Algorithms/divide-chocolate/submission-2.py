class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        N = len(sweetness)

        def verify(val: int) -> bool:
            accum = 0
            count = 0
            for s in sweetness:
                accum += s
                if accum >= val:
                    accum = 0
                    count += 1
            return count >= k + 1

        l, r = min(sweetness), sum(sweetness)
        maxmin = l
        while l <= r:
            mid = (l + r) // 2
            if verify(mid):
                maxmin = max(maxmin, mid)
                l = mid + 1
            else:
                r = mid - 1

        return maxmin