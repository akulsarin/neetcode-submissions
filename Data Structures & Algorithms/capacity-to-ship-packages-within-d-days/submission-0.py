class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N = len(weights)
        
        def canShip(capacity: int) -> bool:
            nDays = 1
            carry = 0
            for w in weights:
                carry += w
                if carry > capacity:
                    carry = w
                    nDays += 1
            return nDays <= days

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res