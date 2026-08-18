class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        minHeap = []
        for srcPort, dstPort, price in flights:
            adj[srcPort].append((price, dstPort))
            if srcPort == src:
                heapq.heappush(minHeap, (price, 0, dstPort))

        minStops = {src: 0}
        while minHeap:
            toPrice, numStops, toLoc = heapq.heappop(minHeap)
            if toLoc == dst:
                return toPrice
            if minStops.get(toLoc, float('inf')) <= numStops:
                continue

            minStops[toLoc] = numStops
            if numStops == k:
                continue
            
            for newPrice, newLoc in adj[toLoc]:
                heapq.heappush(minHeap, (toPrice + newPrice, numStops + 1, newLoc))

        return -1