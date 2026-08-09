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
                minIdx = []
                currProcTime = pendingByProcessing[0][0]
                while pendingByProcessing and pendingByProcessing[0][0] == currProcTime:
                    minIdx.append(heapq.heappop(pendingByProcessing))
                minIdx.sort(key=lambda e: e[-1])
                result.append(minIdx[0][-1])
                for item in minIdx[1:]:
                    heapq.heappush(pendingByProcessing, item)
                time += currProcTime
            else:
                time = availableByStart[0][0]
        
        return result