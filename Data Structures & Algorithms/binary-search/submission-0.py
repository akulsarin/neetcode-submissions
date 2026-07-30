class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid_idx = (l + r) // 2
            print(l, mid_idx, r)
            mid_el = nums[mid_idx]

            if target > mid_el:
                l = mid_idx + 1
            elif target < mid_el:
                r = mid_idx - 1
            else:
                return mid_idx
        
        return -1
        