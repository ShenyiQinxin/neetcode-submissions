# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # sf
    #.s      f
    #        s     f
        # 1  2  3  4
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        i = 0
        while i < n:
            fast = fast.next
            i+=1
        # slow and fast has n distance
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        # slow is at prev, fast.next is None
        if slow and slow.next:
            slow.next = slow.next.next
        return dummy.next


        

        
        