class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counts = Counter(s)
        if len(counts) < k:
            return ""
        
        countsHeap = []
        cooldownHeap = []

        for char, count in counts.items():
            heapq.heappush(countsHeap, (-count, char))
        
        res = []
        while countsHeap or cooldownHeap:
            n = len(res)
            while cooldownHeap and n >= cooldownHeap[0][0]:
                _, count, char = heapq.heappop(cooldownHeap)
                heapq.heappush(countsHeap, (count, char))

            if not countsHeap:
                break

            count, char = heapq.heappop(countsHeap)
            count *= -1
            res.append(char)
            count -= 1
            if count != 0:
                heapq.heappush(cooldownHeap, (n + k, -count, char))

        return "".join(res) if len(res) == len(s) else ""