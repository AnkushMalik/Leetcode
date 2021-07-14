'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root: return False
        if root.val == subRoot.val:
            if self.areTreesEqual(root,subRoot): return True
        leftCheck = self.isSubtree(root.left,subRoot)
        rightCheck = self.isSubtree(root.right,subRoot)
        return leftCheck or rightCheck

    def areTreesEqual(self, root1,root2):
        if not root1 and not root2: return True
        elif (root1 and not root2) or (not root1 and root2): return False
        
        if root1.val !=root2.val:
            return False
        
        if not self.areTreesEqual(root1.left, root2.left) or not self.areTreesEqual(root1.right,root2.right):
            return False
        
        return True
