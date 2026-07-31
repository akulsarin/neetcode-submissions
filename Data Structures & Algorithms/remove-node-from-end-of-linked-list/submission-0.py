# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            length += 2

        if not fast:
            length -= 1

        if n == length:
            return head.next

        target = length - n
        prev, curr = None, head
        while target > 0:
            prev, curr = curr, curr.next
            target -= 1

        prev.next = curr.next
            
        return head

        

        

"""
head = [1,2,3,4,5], n = 2
output = [1,2,3,5]
"""
        