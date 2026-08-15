class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        count = 0
        l = r = 0
        found = l == target
        while not found:
            count += 1
            newL = newR = l + 1
            for i in range(l, r + 1):
                newR = max(newR, i + nums[i])
                if newR >= target:
                    found = True
            l, r = newL, newR
        return count