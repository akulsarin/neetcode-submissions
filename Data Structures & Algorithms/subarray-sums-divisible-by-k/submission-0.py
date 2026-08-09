class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        prefix[j] - prefix[i] = n.k
        => prefix[j] = n.k + prefix[i]
        => prefix[j] (modk) = (n.k (modk) + prefix[i] (modk))(modk)        
        => prefix[j] (modk) = prefix[i](modk)
        """
        counts = defaultdict(int)
        counts[0] += 1
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            remainder = prefix % k
            result += counts[remainder]
            counts[remainder] += 1

        return result
        