class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        minHeap = []
        for fromLoc, toLoc, price in flights:
            adj[fromLoc].append((price, toLoc))
            if fromLoc == src:
                # Sort by priority: price -> stops made
                heapq.heappush(minHeap, (price, 0, toLoc))

        numStops = {src: 0}
        while minHeap:
            price, stopsMade, airport = heapq.heappop(minHeap)
            if airport == dst:
                return price
            
            stopsMade += 1
            if stopsMade > numStops.get(airport, k):
                continue
            numStops[airport] = stopsMade
            for nextPrice, nextAirport in adj[airport]:
                heapq.heappush(minHeap, (price + nextPrice, stopsMade, nextAirport))
        
        return -1