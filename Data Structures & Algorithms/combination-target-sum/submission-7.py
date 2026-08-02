class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        combinations = []

        def dfs(i: int, currComb: List[int], t: int):
            if t == 0:
                combinations.append(currComb.copy())
                return
            elif i == N or t < 0:
                return

            currComb.append(nums[i])
            dfs(i, currComb, t - nums[i])
            currComb.pop()
            dfs(i + 1, currComb, t)

        dfs(0, [], target)
        return combinations

            


        