class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, target: int, curr: List[int], res: List[List[int]]) -> None:
            if target < 0:
                return

            if target == 0:
                res.append(curr.copy())
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j, target-nums[j], curr, res)
                curr.pop()

        res = []
        dfs(0, target, [], res)
        return res        