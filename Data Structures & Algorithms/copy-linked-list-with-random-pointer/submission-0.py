"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldcopy = {None: None}
        p = head
        while p:
            copy = Node(p.val)
            oldcopy[p] = copy
            p = p.next

        p = head
        while p:
            copy = oldcopy[p]
            copy.next = oldcopy[p.next]
            copy.random = oldcopy[p.random]
            p = p.next
        
        return oldcopy[head]
        



        