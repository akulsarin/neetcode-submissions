class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        trapped_water = 0
        l_height, r_height = height[l], height[r]
        while l < r:
            if l_height <= r_height:
                l += 1
                l_height = max(l_height, height[l])
                trapped_water += l_height - height[l]
            else:
                r -= 1
                r_height = max(r_height, height[r])
                trapped_water += r_height - height[r]
        return trapped_water