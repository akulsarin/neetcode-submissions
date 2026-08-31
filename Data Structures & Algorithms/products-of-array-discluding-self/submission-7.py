class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [1] * N
        
        prod = 1
        for i in range(N):
            output[i] *= prod
            prod *= nums[i]
         
        prod = 1
        for i in range(N - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]

        return output