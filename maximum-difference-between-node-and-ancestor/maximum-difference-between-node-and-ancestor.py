# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        path = []
        self.md = 0
        def dfs(root):
            for i in path:
                self.md = max(self.md,abs(root.val-i))
            path.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            path.pop()
        dfs(root)
        return self.md
                