# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = slow, slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        n1, n2 = head, prev
        while n1 != n2:
            nxt = n1.next
            n1.next = n2
            n1, n2 = n2, nxt
        n1.next = None