'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6

'''
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0

        totalCount = self.countUnivalSubtrees(root.left)+self.countUnivalSubtrees(root.right)
        
        if self.isUnival(root):
            totalCount+=1
        return totalCount
    
    def isUnival(self,root):
        if root==None:
            return True
        if not root.left and not root.right:
            return True
        if root.left and root.left.val!=root.val:
            return False
        if root.right and root.right.val!=root.val:
            return False
        if self.isUnival(root.left) and self.isUnival(root.right):
            return True
