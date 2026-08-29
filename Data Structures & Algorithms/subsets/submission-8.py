class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_list = [[]]

        for num in nums:
            current_length = len(subset_list)
            for i in range(current_length):
                subset_copy = subset_list[i].copy()
                subset_copy.append(num)
                subset_list.append(subset_copy)
        
        return subset_list