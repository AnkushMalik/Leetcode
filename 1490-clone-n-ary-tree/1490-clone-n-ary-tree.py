"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        ans = Node(root.val,[]) if root else None
        def dfs(node,orig):
            if not orig: return None
            for i in orig.children:
                node.children.append(Node(i.val,[]))
                dfs(node.children[-1],i)
        dfs(ans,root)
        return ans