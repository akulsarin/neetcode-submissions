class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        permutations = []

        def backtrack(curr: List[int], used: set(int)):
            if len(curr) == N:
                permutations.append(curr.copy())
                return
            
            for num in nums:
                if num not in used:
                    curr.append(num)
                    used.add(num)
                    backtrack(curr, used)
                    used.remove(num)
                    curr.pop()
        
        backtrack([], set())
        return permutations