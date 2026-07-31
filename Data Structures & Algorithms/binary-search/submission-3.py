class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            midNum = nums[mid]
            if target == midNum:
                return mid
            elif target > midNum:
                l = mid + 1
            else:
                r = mid - 1

        return -1

        