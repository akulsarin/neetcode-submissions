class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for num in nums:
            buckets[num] += 1

        i = 0
        for bucket_idx in range(len(buckets)):
            bucket_count = buckets[bucket_idx]
            for _ in range(bucket_count):
                nums[i] = bucket_idx
                i += 1
        