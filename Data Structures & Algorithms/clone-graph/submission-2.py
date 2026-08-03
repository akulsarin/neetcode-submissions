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
            return None

        queue = deque([node])
        cloned = {node: Node(node.val)}

        while queue:
            for _ in range(len(queue)):
                currNode = queue.popleft()
                for neighbor in currNode.neighbors:
                    if neighbor not in cloned:
                        cloned[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)

                    cloned[currNode].neighbors.append(cloned[neighbor])

        return cloned[node]
        