class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        res = []

        def backtrack(i: int, t: int, curr: List[int]):
            if i >= N or t < 0:
                return
            
            if t == 0:
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i, t - nums[i], curr)
            curr.pop()
            backtrack(i + 1, t, curr)

        backtrack(0, target, [])
        return res