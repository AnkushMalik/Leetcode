'''
Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0

'''
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
