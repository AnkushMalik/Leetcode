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
        if not head: return None
        ptr1 = head
        ptr2 = head
        hsh = {}
        while ptr1:
            hsh[ptr1] = Node(ptr1.val)
            ptr1 = ptr1.next
        ans = hsh[head]
        ansptr = ans
        while ptr2:
            if ptr2.next: ansptr.next = hsh[ptr2.next]
            if ptr2.random: ansptr.random = hsh[ptr2.random]
            ptr2 = ptr2.next
            ansptr = ansptr.next
        return ans