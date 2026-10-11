# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # mid point is the slow 
        prev = None
        p = slow.next
        slow.next = None

        while p:
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt

        # prev is the head of the 2nd half
        p1, p2 = head, prev
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        # p1 is one longer
        