class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return True
            
            if nums[l] < nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] == nums[m]:
                l += 1
            elif nums[r] == nums[m]:
                r -= 1

        return False

        