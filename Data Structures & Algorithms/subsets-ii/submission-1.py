class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        result = []

        def dfs(i: int, currSubset: List[int]) -> None:
            if i == N:
                result.append(currSubset.copy())
                return

            currSubset.append(nums[i])
            dfs(i + 1, currSubset)
            currSubset.pop()

            j = i + 1
            while j < N and nums[j] == nums[i]:
                j += 1
            dfs(j, currSubset)

        dfs(0, [])
        return result
        