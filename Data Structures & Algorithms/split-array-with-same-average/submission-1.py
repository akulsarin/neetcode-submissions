class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        
        dp = [set() for _ in range(N // 2 + 1)]
        dp[0].add(0)

        for num in nums:
            for l in range (N // 2, 0, -1):
                for prevSum in dp[l - 1]:
                    dp[l].add(prevSum + num)

        for size, sums in enumerate(dp[1:], start=1):
            for sizeSum in sums:
                if sizeSum == (total * size) / N:
                    return True

        return False
