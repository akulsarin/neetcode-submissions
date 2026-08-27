class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        
        counts = Counter(nums)
        buckets = [[] for _ in range(N + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        top_k = []
        for count in range(N, -1, -1):
            top_k.extend(buckets[count])
            if len(top_k) >= k:
                break
        return top_k[:k]