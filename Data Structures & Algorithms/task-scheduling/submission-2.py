class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        
        min_heap = [-count for count in counts.values()]
        heapq.heapify(min_heap)
        cooldown = deque()
        cycles = 0
        
        while min_heap or cooldown:
            cycles += 1
            if cooldown and not min_heap:
                cycles = cooldown[0][0]

            if min_heap:
                neg_count = heapq.heappop(min_heap)
                count = (neg_count * -1) - 1
                if count > 0:
                    cooldown.append((cycles + n, count))
            
            while cooldown and cycles >= cooldown[0][0]:
                _, count = cooldown.popleft()
                heapq.heappush(min_heap, -count)
        
        return cycles