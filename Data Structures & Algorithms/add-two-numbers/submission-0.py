# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        carry = 0
        while l1 or l2 or carry:
            result.next = ListNode()
            result = result.next

            if not l1:
                l1 = ListNode(val=0)
            if not l2:
                l2 = ListNode(val=0)

            digitSum = l1.val + l2.val + carry
            result.val = digitSum % 10
            if digitSum > 9:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next


        return dummy.next
            


        