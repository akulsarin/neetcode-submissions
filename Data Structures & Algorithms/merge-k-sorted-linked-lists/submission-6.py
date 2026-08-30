# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        merged_list = dummy

        min_heap = [(lst.val, i) for i, lst in enumerate(lists) if lst is not None]
        heapq.heapify(min_heap)

        while min_heap:
            curr_min, idx = heapq.heappop(min_heap)
            merged_list.next = ListNode(curr_min)
            merged_list = merged_list.next

            lists[idx] = lists[idx].next
            if lists[idx] is not None:
                heapq.heappush(min_heap, (lists[idx].val, idx))

        return dummy.next