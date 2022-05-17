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
        if original.left:
            leftAns = self.getTargetCopy(original.left, cloned.left, target)
            if leftAns: ans = leftAns
        if original.right:
            rightAns = self.getTargetCopy(original.right, cloned.right, target)
            if rightAns: ans = rightAns
        return ans
            
            