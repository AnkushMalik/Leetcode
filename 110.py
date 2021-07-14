'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True
        self.checkBalance(root)
        return self.balanced
    
    def checkBalance(self,root):
        if not root: return 0
        ltdist,rtdist = 0,0
        
        if root.left:
            ltdist += 1 + self.checkBalance(root.left)
        if root.right:
            rtdist += 1+self.checkBalance(root.right)
        if abs(rtdist-ltdist)>1:
            self.balanced = False
        return max(ltdist,rtdist)
