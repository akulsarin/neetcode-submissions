# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode(next=head)
        start = dummy
        end = head
        idx = 0
        while end:
            idx += 1
            if idx % k == 0:
                nextNode = end.next
                prev, curr = start.next, start.next.next
                start.next = end
                prev.next = end.next
                start = prev
                while curr != nextNode:
                    next = curr.next
                    curr.next = prev
                    prev, curr = curr, next
                end = start
            end = end.next
        return dummy.next