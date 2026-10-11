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
        map1 = {None: None} # node : node's copy
        
        p = head
        while p:
            map1[p] = Node(p.val)
            p = p.next

        p = head
        while p:
            clone = map1[p]
            clone.next = map1[p.next]
            clone.random = map1[p.random]
            p = p.next
        return map1[head]

        