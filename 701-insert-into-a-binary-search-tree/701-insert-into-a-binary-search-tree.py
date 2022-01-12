# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        def goToRoot(root):
            if root.val>val:
                if root.left: goToRoot(root.left)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right: goToRoot(root.right)
                else:
                    root.right = TreeNode(val)
        test = goToRoot(root)
        return root