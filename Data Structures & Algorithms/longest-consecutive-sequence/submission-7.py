class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in uniqueNums:
                itr = num + 1
                while itr in uniqueNums:
                    itr += 1
                res = max(res, itr - num)

        return res
        