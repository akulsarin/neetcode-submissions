class MedianFinder:

    def __init__(self):
        # Contains roughly half of the smallest values seen (maxHeap)
        self.small = []

        # Contains roughly half of the largest values seen (minHeap)
        self.large = []
        

    def addNum(self, num: int) -> None:
        # First, we arbitrarily add `num` to the min-heap
        heapq.heappush(self.small, -num)

        # If this was the first insertion, nothing else is needed
        if len(self.small) == 1:
            return

        # Then, we check the following:
        # 1. The ordering property is satisfied, i.e., maxHeap[0] <= minHeap[0]
        # 2. The maxHeap is no more than one larger than the minHeap
        # If either of these is violated, we pop from maxHeap and push to minHeap
        if len(self.small) > len(self.large) + 1 or -self.small[0] > self.large[0]:
            maxSmall = -heapq.heappop(self.small)
            heapq.heappush(self.large, maxSmall)
        
        # Then, we check if the minHeap is no more than one larger than the maxHeap
        # If not, we pop from minHeap and push to maxHeap
        if len(self.large) > len(self.small) + 1:
            minLarge = heapq.heappop(self.large)
            heapq.heappush(self.small, -minLarge)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2
        