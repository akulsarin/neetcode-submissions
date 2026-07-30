class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        seqLens = {}
        res = 0

        for num in nums:
            if num - 1 not in uniqueNums:
                seqLens[num] = 1
                itr = num + 1
                while itr in uniqueNums:
                    seqLens[num] += 1
                    itr += 1
                res = max(res, seqLens[num])

        return res
        