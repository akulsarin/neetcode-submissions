class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        subset_list = []

        def backtrack(i: int, curr: List[int]):
            if i == N:
                subset_list.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return subset_list