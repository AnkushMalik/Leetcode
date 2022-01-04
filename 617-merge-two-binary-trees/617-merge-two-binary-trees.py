# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        def dfs(r1,r2):
            if not r2: return r1
            r1.val+=r2.val
            if r1.left:
                r1.left = dfs(r1.left, r2.left)
            else:
                r1.left = r2.left
            if r1.right:
                r1.right = dfs(r1.right,r2.right)
            else:
                r1.right = r2.right
            return r1
        return dfs(root1,root2)