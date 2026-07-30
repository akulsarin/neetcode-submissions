class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int, curr: List[int], res: List[int]):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr, res)
            curr.pop()
            dfs(i + 1, curr, res)

        res = []
        dfs(0, [], res)
        return res
        