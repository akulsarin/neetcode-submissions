class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            days_taken = 1
            weight_added = 0
            for weight in weights:
                if weight_added + weight > capacity:
                    days_taken += 1
                    weight_added = 0
                weight_added += weight
            return days_taken <= days

        l, r = max(weights), sum(weights)
        min_cap = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if can_ship(mid):
                min_cap = min(min_cap, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_cap