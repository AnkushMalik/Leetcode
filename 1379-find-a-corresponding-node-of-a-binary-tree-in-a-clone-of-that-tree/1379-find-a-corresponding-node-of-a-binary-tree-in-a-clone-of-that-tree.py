# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original==target: return cloned
        ans = None
        if original.left and self.getTargetCopy(original.left, cloned.left, target): 
            ans = self.getTargetCopy(original.left, cloned.left, target)
        if original.right and self.getTargetCopy(original.right, cloned.right, target): 
            ans = self.getTargetCopy(original.right, cloned.right, target)
        return ans
            
            