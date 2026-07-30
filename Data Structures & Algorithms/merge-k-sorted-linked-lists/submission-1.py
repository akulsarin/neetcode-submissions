# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = ListNode()
        curr = sorted_list
        num_terminated = 0

        while num_terminated < len(lists):
            min_val = float('inf')
            min_val_idx = -1
            for i in range(len(lists)):
                lst = lists[i]
                if not lst:
                    continue
                if lst.val < min_val:
                    min_val = lst.val
                    min_val_idx = i
            
            curr.next = ListNode(val=min_val)
            lists[min_val_idx] = lists[min_val_idx].next
            if not lists[min_val_idx]:
                num_terminated += 1

            curr = curr.next

        return sorted_list.next 

            



        