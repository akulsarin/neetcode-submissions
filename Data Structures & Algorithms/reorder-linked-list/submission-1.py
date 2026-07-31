# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, next = slow, slow.next
        while next:
            temp = next.next
            next.next = curr
            curr, next = next, temp

        p1, p2 = head, curr
        while p1 != p2:
            temp = p1.next
            p1.next = p2
            p1, p2 = p2, temp
        p1.next = None

"""
input  = [0, 1, 2, 3, 4, 5]
output = [0, 5, 1, 4, 2, 3]
"""