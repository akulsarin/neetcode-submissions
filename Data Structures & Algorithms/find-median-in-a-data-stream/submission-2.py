class MedianFinder:

    def __init__(self):
        self.minHeap = [] # Contains roughly half of the largest values in ascending order
        self.maxHeap = [] # Contains roughly half of the smallest values in descending order
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        if self.maxHeap and num < -self.maxHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)

        while abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else: 
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        
        