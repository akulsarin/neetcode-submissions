class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        availableByStart = []
        pendingByProcessing = []

        for i, task in enumerate(tasks):
            heapq.heappush(availableByStart, (task[0], task[1], i))

        time = availableByStart[0][0]
        result = []
        while availableByStart or pendingByProcessing:
            # 1. If CPU is idle, fast-forward time to the next task's start time
            if not pendingByProcessing and availableByStart:
                time = max(time, availableByStart[0][0])
            
            while availableByStart and availableByStart[0][0] <= time:
                _, procTime, index = heapq.heappop(availableByStart)
                heapq.heappush(pendingByProcessing, (procTime, index))

            procTime, idx = heapq.heappop(pendingByProcessing)
            result.append(idx)
            time += procTime
        
        return result