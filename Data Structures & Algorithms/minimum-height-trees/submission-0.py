class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dp = [[0] * 2 for _ in range(n)]

        def postOrder(parent: int, curr: int):
            downwardLens = [0, 0]
            for child in adj[curr]:
                if child != parent:
                    postOrder(curr, child)
                    downwardLens.append(1 + dp[child][0])

            topTwo = heapq.nlargest(2, downwardLens)
            dp[curr][0], dp[curr][1] = topTwo[0], topTwo[1]

            return dp[curr][0]

        def preOrder(parent: int, curr: int, topHeight: int):
            if topHeight > dp[curr][0]:
                dp[curr][1] = dp[curr][0]
                dp[curr][0] = topHeight
            elif topHeight > dp[curr][1]:
                dp[curr][1] = topHeight

            for child in adj[curr]:
                if child != parent:
                    if dp[curr][0] == 1 + dp[child][0]:
                        preOrder(curr, child, 1 + dp[curr][1])
                    else:
                        preOrder(curr, child, 1 + dp[curr][0])

        
        postOrder(-1, 0)
        preOrder(-1, 0, 0)
        min_height = min(dp[i][0] for i in range(n))
        return [i for i in range(n) if dp[i][0] == min_height]