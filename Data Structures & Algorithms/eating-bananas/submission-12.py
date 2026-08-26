import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_bananas(k: int) -> bool:
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile / k)
            return hours_taken <= h

        l, r = 1, max(piles)
        min_k = r
        while l <= r:
            k = (l + r) // 2
            if can_eat_bananas(k):
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1
        
        return min_k