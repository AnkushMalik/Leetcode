'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.checkSymmetric(root.left,root.right)
    
    def checkSymmetric(self,leftNode,rightNode):
        if not leftNode or not rightNode:
            return leftNode==rightNode
        if leftNode.val!=rightNode.val:
            return False
        
        return self.checkSymmetric(leftNode.left,rightNode.right) and self.checkSymmetric(leftNode.right,rightNode.left)
        
