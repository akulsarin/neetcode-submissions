class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = []

        def dfs(currPerm: List[int], picked: List[bool]) -> None:
            if len(currPerm) == N:
                result.append(currPerm.copy())
                return

            for i, num in enumerate(nums):
                if not picked[i]:
                    currPerm.append(num)
                    picked[i] = True
                    dfs(currPerm, picked)
                    picked[i] = False
                    currPerm.pop()
            
        dfs([], [False] * N)
        return result
