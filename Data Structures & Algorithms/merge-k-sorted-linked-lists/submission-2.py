# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode()
        curr = dummy
        numRemaining = len(lists)

        while numRemaining > 0:
            minVal = float('inf')
            minIdx = None
            for i, node in enumerate(lists):
                if not node:
                    continue
                    
                if node.val < minVal:
                    minVal = node.val
                    minIdx = i

            curr.next = ListNode(minVal)
            curr = curr.next

            lists[minIdx] = lists[minIdx].next
            if not lists[minIdx]:
                numRemaining -= 1

        return dummy.next

            





        