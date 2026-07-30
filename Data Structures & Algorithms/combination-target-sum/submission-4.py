class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = [] 
        nums.sort()
        
        def dfs(i, target):
            if target < 0:
                return
            
            if target == 0:
                res.append(subset.copy())
                return

            for j in range(i, len(nums)):
                num = nums[j]
                subset.append(num)
                dfs(j, target - num)
                subset.pop()

        dfs(0, target)
        return res
        