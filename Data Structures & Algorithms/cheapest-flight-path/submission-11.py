class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj[from_i].append((price_i, to_i))

        min_heap = [(0, 0, src)]
        num_stops = {}
        while min_heap:
            price_i, stop_count, to_i = heapq.heappop(min_heap)
            
            if to_i == dst: 
                return price_i
            
            if stop_count > k or stop_count >= num_stops.get(to_i, float('inf')):
                continue

            num_stops[to_i] = stop_count
            for next_price, next_dst in adj[to_i]:
                heapq.heappush(min_heap, (price_i + next_price, stop_count + 1, next_dst))

        return -1