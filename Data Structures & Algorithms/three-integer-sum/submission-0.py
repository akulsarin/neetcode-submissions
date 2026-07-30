class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()

        triplets = set()

        for anchor in range(N):
            anchorEl = nums[anchor]
            l, r = anchor + 1, N - 1
            while l < r:
                combinationSum = nums[l] + nums[r] + anchorEl

                if combinationSum < 0:
                    l += 1
                elif combinationSum > 0:
                    r -= 1
                else:
                    triple = [anchorEl, nums[l], nums[r]]
                    triple.sort()
                    triplets.add(tuple(triple))
                    l += 1
                    r -= 1
            
        
        return [list(triple) for triple in triplets]              

        