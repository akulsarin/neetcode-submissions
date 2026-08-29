class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        perms = []

        def dfs(curr: List[int], indices_used: set[int]):
            if len(curr) == N:
                perms.append(curr.copy())
                return
            
            for i in range(N):
                if i not in indices_used:
                    indices_used.add(i)
                    curr.append(nums[i])
                    dfs(curr, indices_used)
                    curr.pop()
                    indices_used.remove(i)
        
        dfs([], set())
        return perms