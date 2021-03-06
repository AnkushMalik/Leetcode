'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false
'''

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if(not root):
            return False
        if(not root.left and not root.right):
            return True if targetSum==root.val else False
        leftSum = self.hasPathSum(root.left, targetSum-root.val) if root.left else False
        rightSum = self.hasPathSum(root.right, targetSum-root.val) if root.right else False
        
        return bool(leftSum+rightSum)
