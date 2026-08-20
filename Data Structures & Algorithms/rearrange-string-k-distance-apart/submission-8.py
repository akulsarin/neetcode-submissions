class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counts = Counter(s)        
        countsHeap = []
        cooldownQ = deque([])

        for char, count in counts.items():
            heapq.heappush(countsHeap, (-count, char))
        
        res = []
        while countsHeap or cooldownQ:
            n = len(res)
            while cooldownQ and n >= cooldownQ[0][0]:
                _, count, char = cooldownQ.popleft()
                heapq.heappush(countsHeap, (count, char))

            if not countsHeap:
                break

            count, char = heapq.heappop(countsHeap)
            count *= -1
            res.append(char)
            count -= 1
            if count != 0:
                cooldownQ.append((n + k, -count, char))

        return "".join(res) if len(res) == len(s) else ""