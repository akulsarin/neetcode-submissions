class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = [] 
        
        def dfs(target):
            if target < 0:
                return
            elif target == 0:
                subset_sorted = sorted(subset)
                if subset_sorted not in res:
                    res.append(subset_sorted)
            else:
                for num in nums:
                    subset.append(num)
                    dfs(target - num)
                    subset.pop()

        dfs(target)
        return res
        