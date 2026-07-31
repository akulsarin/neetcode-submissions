# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        sumHead = ListNode()
        sumTracker = sumHead
        carry = 0
        while l1 or l2 or carry:
            l1 = l1 or dummy
            l2 = l2 or dummy

            d1, d2 = l1.val, l2.val 
            result = d1 + d2 + carry
            sumVal, carry = result % 10, result // 10

            sumTracker.next = ListNode(sumVal)
            sumTracker = sumTracker.next

            l1 = l1.next
            l2 = l2.next

        return sumHead.next