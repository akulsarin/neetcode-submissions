# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        degenerate_node = ListNode()
        sum_list = ListNode()
        
        curr = sum_list
        carry = 0
        while l1 or l2 or carry:
            l1 = l1 or degenerate_node
            l2 = l2 or degenerate_node
            
            sum_val = l1.val + l2.val + carry
            curr_val, carry = sum_val % 10, sum_val // 10

            l1, l2 = l1.next, l2.next
            curr.next = ListNode(val=curr_val)
            curr = curr.next

        return sum_list.next