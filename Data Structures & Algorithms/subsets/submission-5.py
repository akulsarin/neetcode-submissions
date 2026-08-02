class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        uniqueSubsets = []

        def dfs(i: int, currSubset: List[int]):
            if i == N:
                uniqueSubsets.append(currSubset.copy())
                return

            currSubset.append(nums[i])
            dfs(i + 1, currSubset)
            currSubset.pop()
            dfs(i + 1, currSubset)

        dfs(0, [])
        return uniqueSubsets