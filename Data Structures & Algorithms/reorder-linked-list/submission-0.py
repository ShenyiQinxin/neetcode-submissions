# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
      
      
        #.    m
        # 2,4,6,8,10
        prev = None
        # mid is slow
        # reverse 2nd half
        p = slow.next
        slow.next = None
        while p:
            tmp = p.next
            p.next = prev
            prev = p
            p = tmp

        # interleaving
        p1 = head
        p2 = prev
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next = p2 
            p2.next = tmp1 
            
            # advance
            p1 = tmp1
            p2 = tmp2




        