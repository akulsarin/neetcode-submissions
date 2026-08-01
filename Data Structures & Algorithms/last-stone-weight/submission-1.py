class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest1 = heapq.heappop(stones)
            heaviest2 = heapq.heappop(stones)

            if heaviest1 == heaviest2:
                continue

            heapq.heappush(stones, -abs(heaviest1 - heaviest2))

        if stones:
            return -stones[0]

        return 0
        