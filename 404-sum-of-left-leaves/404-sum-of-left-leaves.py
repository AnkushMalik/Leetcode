# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 0
        return self.calcSumOfLL(root)
    
    def calcSumOfLL(self, root):
        if not root: return 0
        if not root.left and not root.right:
            return root.val
        sumLeft = self.calcSumOfLL(root.left) if root.left else 0
        sumLeft += self.calcSumOfLL(root.right) if root.right and (root.right.left or root.right.right) else 0
        return sumLeft