import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours_for_pile(pile_count: int, k: int) -> int:
            return math.ceil(pile_count / k)

        def total_hours(k: int) -> int:
            return sum([hours_for_pile(pile_count, k) for pile_count in piles])

        def is_correct(k: int) -> int:
            hours_taken = total_hours(k)
            if hours_taken > h:
                return -1
            elif hours_taken <= h:
                return 1

        l, r = 1, max(piles)

        min_k = float('inf')
        while l <= r:
            mid = (l + r) // 2
            result = is_correct(mid)

            if result > 0:
                r = mid - 1
                min_k = mid
            elif result < 0:
                l = mid + 1

        return min_k