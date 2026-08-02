class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxFreqHeap = []
        for task, freq in counts.items():
            heapq.heappush(maxFreqHeap, [-freq, task])

        queue = deque([])
        time = 0
        while maxFreqHeap or queue:
            if maxFreqHeap:
                freq, task = heapq.heappop(maxFreqHeap)
                freq = -freq - 1
                if freq != 0:
                    queue.append([freq, time + n, task])
            else:
                time = queue[0][1]

            if queue and queue[0][1] == time:
                newFreq, _, task = queue.popleft()
                heapq.heappush(maxFreqHeap, [-newFreq, task])

            time += 1
        
        return time






        