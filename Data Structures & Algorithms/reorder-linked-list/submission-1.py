# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # fast.next is None
        # slow is the mid

        prev = None
        p = slow.next
        slow.next = None

        while p:
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
        
        # interleaving
        p1 = head
        p2 = prev
        # the 2nd half is equal or shorter
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next = p2
            p2.next = tmp1

            p1 = tmp1
            p2 = tmp2





        