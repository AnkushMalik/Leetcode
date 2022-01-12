# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        def goToRoot(root,val):
            if root.val>val:
                return goToRoot(root.left,val) if root.left else root
            else:
                return goToRoot(root.right,val) if root.right else root
        test = goToRoot(root,val)
        if test.val>val:
            test.left = TreeNode(val)
        else:
            test.right = TreeNode(val)
        return root