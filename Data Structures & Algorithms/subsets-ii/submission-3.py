class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        subsets = []

        def backtrack(i: int, curr: List[int]):
            if i == N:
                subsets.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            
            j = i + 1
            while j < N and nums[j] == nums[i]:
                j += 1
            backtrack(j, curr)

        backtrack(0, [])
        return subsets