"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        nodes = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neighbor in curr.neighbors:
                    if neighbor not in nodes:
                        nodes[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                    nodes[curr].neighbors.append(nodes[neighbor])
        
        return nodes[node]