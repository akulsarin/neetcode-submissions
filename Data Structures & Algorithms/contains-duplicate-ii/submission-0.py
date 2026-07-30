class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return False

        l = 0
        window = {nums[l]}

        for r in range(1, n):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            
            if nums[r] in window:
                return True

            window.add(nums[r])

        return False
            




        