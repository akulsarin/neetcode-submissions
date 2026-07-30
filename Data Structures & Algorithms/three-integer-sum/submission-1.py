class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()

        triplets = []

        for i, anchor in enumerate(nums):
            if anchor > 0:
                break
            
            if (i > 0 and anchor == nums[i - 1]):
                continue
            
            l, r = i + 1, N - 1
            while l < r:
                combinationSum = nums[l] + nums[r] + anchor

                if combinationSum < 0:
                    l += 1
                elif combinationSum > 0:
                    r -= 1
                else:
                    triplets.append([anchor, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        
        return triplets         

        