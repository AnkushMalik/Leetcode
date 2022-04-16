# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode], carry=0) -> Optional[TreeNode]:
        if not root: return root
        if not root.right:
            root.val+=carry
        if root.right:
            self.convertBST(root.right, carry)
            rtSmallest = self.findSmallest(root.right)
            root.val += rtSmallest.val
        if root.left: self.convertBST(root.left, root.val)
        return root
    
    def findSmallest(self, node):
        if node.left:
            return self.findSmallest(node.left)
        return node