class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)

        result = []
        for item in reversed(freq):
            result.extend(item)
            if len(result) >= k:
                result = result[:k]
                break

        return result
        