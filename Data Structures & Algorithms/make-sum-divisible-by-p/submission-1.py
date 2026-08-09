class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Find the smallest subarray 'sub' such that:

        (sum(nums) - sum(sub)) (mod p) = 0
        => sum(nums) - sum(sub) = k.p, for some k > 0
        => sum(sub) = sum(nums) - k.p

        Let total := sum(nums) and sum(sub) = prefix[j] - prefix[i] {where i, j and the endpoints of the subarray 'sub'}
        => prefix[j] - prefix[i] = total - k.p
        => prefix[j] = prefix[i] + total - k.p
        => prefix[j] (mod p) = ((prefix[i] + total) (mod p) - k.p (mod p)) (mod.p)
        => prefix[j] (mod p) = (prefix[i] + total) (mod p)
        """

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