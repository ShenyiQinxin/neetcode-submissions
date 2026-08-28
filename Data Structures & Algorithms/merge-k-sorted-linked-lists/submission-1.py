# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(10000000000)
        p = dummy
        minheap = []
        counter = 0
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap, (lists[i].val, counter, lists[i]))
                counter+=1

        while minheap:
            curr = heapq.heappop(minheap)
            p.next = curr[2]
            p = p.next
            
            if curr[2].next:
                heapq.heappush(minheap, (curr[2].next.val, counter, curr[2].next))
                counter += 1
        return dummy.next

            





        