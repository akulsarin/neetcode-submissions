class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEat(k: int) -> int:
            t = 0
            for numBananas in piles:
                t += numBananas // k
                if numBananas % k != 0:
                    t += 1
            return t

        l, r = 1, max(piles)

        bestK = r
        while l <= r:
            mid = (l + r) // 2
            t = timeToEat(mid)
            if t > h:
                l = mid + 1
            elif t <= h:
                bestK = mid
                r = mid - 1
            # else:
            #     return mid

        return bestK
