# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, startNode: ListNode, k: int) -> ListNode:
        """
        Reverse 1 group of k nodes, starting at `startNode`.
        Assumes there are at least k nodes starting from `startNode`.
        Returns the new starting node for this group.
        """
        prev, curr = None, startNode
        counter = k
        while counter > 0:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
            counter -= 1

        newStartNode = prev
        startNode.next = curr
        return newStartNode

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        numGroups = length // k

        prev, curr = None, head
        newHead = None
        while numGroups > 0:
            reversedHead = self.reverseGroup(curr, k)
            if not newHead:
                newHead = reversedHead
            if prev:
                prev.next = reversedHead
            prev, curr = curr, curr.next
            numGroups -= 1

        return newHead

            


        