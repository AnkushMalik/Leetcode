"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root: return ans
        def bfs(root):
            ans.append(root.val)
            for i in root.children:
                if i: bfs(i)
        bfs(root)
        return ans