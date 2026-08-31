class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, edge in enumerate(edges):
            node_1, node_2 = edge
            prob = succProb[i]
            adj[node_1].append((prob, node_2))
            adj[node_2].append((prob, node_1))

        min_heap = [(-1, start_node)]
        visited = set()
        while min_heap:
            path_prob, node = heapq.heappop(min_heap)
            if node == end_node:
                return -path_prob
            if node in visited:
                continue
            visited.add(node)
            
            for next_prob, neighbor in adj[node]:
                heapq.heappush(min_heap, (path_prob * next_prob, neighbor))

        return 0