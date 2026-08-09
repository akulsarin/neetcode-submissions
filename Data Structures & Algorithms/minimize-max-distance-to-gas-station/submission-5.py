class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        N = len(stations)

        def isPossible(dist: float) -> bool:
            count = 0
            for i in range(N - 1):
                x1, x2 = stations[i], stations[i + 1]
                count += (x2 - x1) // dist
            return count <= k

        low, high = 0, 1e8
        while high - low > 1e-6:
            mid = (low + high) / 2
            if isPossible(mid):
                high = mid
            else:
                low = mid
        return low

        