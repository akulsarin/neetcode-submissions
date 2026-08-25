class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        products = [1] * N

        # Left pass
        leftProd = nums[0]
        for i in range(1, N):
            products[i] *= leftProd
            leftProd *= nums[i] 

        # Right pass
        rightProd = nums[-1]
        for i in range(N - 2, -1, -1):
            products[i] *= rightProd
            rightProd *= nums[i]
        
        return products