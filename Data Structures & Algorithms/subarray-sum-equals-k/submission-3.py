class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        target_counts = defaultdict(int)
        target_counts[k] = 1
        
        prefix = 0
        total = 0
        for num in nums:
            prefix += num
            total += target_counts[prefix]
            target_counts[prefix + k] += 1

        return total 