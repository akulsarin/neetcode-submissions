class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        products = [1] * N

        # Left pass
        left_prod = 1
        for i in range(N):
            products[i] *= left_prod
            left_prod *= nums[i] 

        # Right pass
        right_prod = 1
        for i in range(N - 1, -1, -1):
            products[i] *= right_prod
            right_prod *= nums[i]
        
        return products