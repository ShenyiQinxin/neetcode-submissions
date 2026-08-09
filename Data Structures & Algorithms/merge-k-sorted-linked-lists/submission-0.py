# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        p = dummy = ListNode(-90000)
        
        minheap = []

        counter = 0
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap, (lists[i].val, counter, lists[i]))
                counter += 1
        
        while minheap:
            tmp = heapq.heappop(minheap)
            
            p.next = tmp[2]
            p = p.next

            if tmp[2].next:
                heapq.heappush(minheap, (tmp[2].next.val, counter, tmp[2].next))
                counter += 1
        return dummy.next





        