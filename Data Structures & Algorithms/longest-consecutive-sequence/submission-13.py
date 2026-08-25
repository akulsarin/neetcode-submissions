class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        len_seq = 0
        
        for num in unique_nums:
            if num - 1 in unique_nums:
                continue
            
            count = 1
            while num + 1 in unique_nums:
                count += 1
                num += 1
            len_seq = max(len_seq, count)
            
        return len_seq