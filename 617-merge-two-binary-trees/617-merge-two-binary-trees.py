# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r1,r2):
            if not r1 and not r2:
                return None
            a = b = 0
            if r1:
                a = r1.val
            if r2:
                b = r2.val
            root = TreeNode(a+b)
            root.left = dfs(r1 and r1.left, r2 and r2.left)
            root.right = dfs(r1 and r1.right, r2 and r2.right)
            return root
        return dfs(root1,root2)