class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        prefix = [1] * N
        for i in range(1, N):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = [1] * N
        for i in range(N - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        return [pre * post for pre, post in zip(prefix, postfix)]