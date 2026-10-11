# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, dummy
        while n > 0:
            fast = fast.next
            n-=1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # slow is 2 and fast is 4, remove 3
        slow.next = slow.next.next
        return dummy.next
            
        