"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        arr = [root]
        while arr:
            temp = []
            while arr:
                ptr = arr.pop(0)
                ptr.next = arr[0] if arr else None
                if ptr.left:
                    temp.append(ptr.left)
                    temp.append(ptr.right)
            arr = temp
        return root
                
                     
                    
                