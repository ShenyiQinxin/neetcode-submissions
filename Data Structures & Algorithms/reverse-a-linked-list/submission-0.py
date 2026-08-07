# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = prev = None
        p = head

        while p:
            tmp = p.next
            p.next = prev
            prev = p
            p = tmp
        return prev