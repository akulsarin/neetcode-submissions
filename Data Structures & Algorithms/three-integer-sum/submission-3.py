class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        three_sum_triplets = []
        i = 0
        while i + 2 < n:
            l, r = i + 1, n - 1
            while l < r:
                triplet_sum = nums[i] + nums[l] + nums[r]
                
                if triplet_sum < 0:
                    l += 1
                elif triplet_sum > 0:
                    r -= 1
                else:
                    three_sum_triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1

        return three_sum_triplets