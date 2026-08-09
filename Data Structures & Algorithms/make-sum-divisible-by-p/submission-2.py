class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        total = sum(nums)
        prefixStore = defaultdict(int)

        remainder = total % p
        if remainder == 0:
            return 0
        
        prefixStore[remainder] = -1
        prefix = 0
        minSoFar = float('inf')
        for r, num in enumerate(nums):
            prefix += num
            query = prefix % p
            if query in prefixStore:
                l = prefixStore[query]
                print(l, r)
                minSoFar = min(minSoFar, r - l)
            key = (prefix + total) % p
            prefixStore[key] = r

        if minSoFar >= N:
            return -1

        return minSoFar