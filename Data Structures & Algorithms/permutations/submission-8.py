class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        perms = []

        def dfs(curr: List[int], used: set[int]):
            if len(curr) == N:
                perms.append(curr.copy())
                return
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    curr.append(num)
                    dfs(curr, used)
                    curr.pop()
                    used.remove(num)
        
        dfs([], set())
        return perms