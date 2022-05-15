"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        def dfs(node):
            if not node.children: return [node.val]
            childAns = []
            for i in node.children:
                childAns += dfs(i)
            return childAns+[node.val]
        return dfs(root)