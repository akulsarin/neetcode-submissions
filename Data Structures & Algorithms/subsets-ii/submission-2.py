class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        subsets = []

        def backtrack(i: int, curr: List[int]):
            if i == N:
                subsets.append(curr.copy())
                return
            
            j = i + 1
            while j < N and nums[j] == nums[i]:
                j += 1

            # Don't use this num
            backtrack(j, curr)

            # Use all possible counts of this number
            for _ in range(i, j):
                curr.append(nums[i])
                backtrack(j, curr)

            for _ in range(i, j):
                curr.pop()

        backtrack(0, [])
        return subsets