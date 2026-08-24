# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        sz = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            sz += 2
        if not fast:
            sz -= 1
        
        if n == sz:
            return head.next

        prev, curr = None, head
        for _ in range(sz - n):
            prev, curr = curr, curr.next

        prev.next = curr.next
        return head