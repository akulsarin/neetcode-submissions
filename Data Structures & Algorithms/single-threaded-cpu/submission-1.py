class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        availableByStart = []
        pendingByProcessing = []

        for i, task in enumerate(tasks):
            heapq.heappush(availableByStart, (task[0], task[1], i))

        time = availableByStart[0][0]
        result = []
        while availableByStart or pendingByProcessing:
            while availableByStart and availableByStart[0][0] <= time:
                _, procTime, index = heapq.heappop(availableByStart)
                heapq.heappush(pendingByProcessing, (procTime, index))

            prev = -1
            if pendingByProcessing:
                procTime, idx = heapq.heappop(pendingByProcessing)
                result.append(idx)
                time += procTime
            else:
                time = availableByStart[0][0]
        
        return result