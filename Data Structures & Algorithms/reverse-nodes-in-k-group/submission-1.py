# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = dummy = ListNode(-1)
        dummy.next = head

        while p:
            kth = p
            counter = k
            while counter > 0 and kth:
                kth = kth.next
                counter -= 1
            if kth:
                groupNext = kth.next
            else:
                break
            
            prev = groupNext
            curr = p.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp1 = p.next # node 1 
            p.next = kth # node 3, the head is official
            p = tmp1
        return dummy.next

            
            


        