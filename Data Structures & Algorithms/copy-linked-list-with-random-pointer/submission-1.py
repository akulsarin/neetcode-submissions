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
        node_map = {None: None}
        
        # Make the copies
        curr = head
        while curr:
            curr_copy = Node(curr.val)
            node_map[curr] = curr_copy
            curr = curr.next
        
        # Set the pointers
        curr = head
        while curr:
            node_map[curr].next = node_map[curr.next]
            node_map[curr].random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]