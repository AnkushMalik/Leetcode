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
            lim = len(arr)
            i = 0
            while i<lim:
                ptr = arr.pop(0)
                ptr.next = arr[0] if i<lim-1 else None
                if ptr.left:
                    arr.append(ptr.left)
                    arr.append(ptr.right)
                i+=1
        return root
                
                     
                    
                