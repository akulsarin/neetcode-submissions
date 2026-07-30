# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        prev = slow

        while fast:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        currSum = 0
        forw, back = slow, prev
        while forw and prev:
            currSum = max(currSum, forw.val + prev.val)
            forw = forw.next
            prev = prev.next
        
    
        return currSum