class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        min_heap = []
        output = [-1] * len(queries)
        i = 0 
        
        for q, original_idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1
                
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
                
            if min_heap:
                output[original_idx] = min_heap[0][0]
                
        return output