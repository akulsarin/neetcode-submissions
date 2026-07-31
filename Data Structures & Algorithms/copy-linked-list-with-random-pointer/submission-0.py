"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        headCopy = None
        nodeMap = {}
        while curr:
            nodeCopy = Node(curr.val)
            nodeMap[curr] = nodeCopy
            if not headCopy:
                headCopy = nodeCopy
            curr = curr.next

        for nodeOriginal, nodeCopy in nodeMap.items():
            nodeCopy.next = nodeMap.get(nodeOriginal.next)
            nodeCopy.random = nodeMap.get(nodeOriginal.random)

        return headCopy

        
        