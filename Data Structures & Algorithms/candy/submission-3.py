class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        numCandies = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                numCandies[i] += numCandies[i - 1]
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                numCandies[i] = max(numCandies[i], numCandies[i + 1] + 1)
        return sum(numCandies)