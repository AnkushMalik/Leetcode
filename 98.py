'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        def checkChildVals(root,target,checkSmall):
            if not root:
                return True
            if checkSmall:
                if root.val>=target:
                    return False
            else:
                if root.val<=target:
                    return False
            return checkChildVals(root.left,target,checkSmall)*checkChildVals(root.right,target,checkSmall)
        
        isBST = checkChildVals(root.left,root.val,True)
        if not isBST: return False
        isBST*=checkChildVals(root.right,root.val,False)
        if not isBST: return False
        return isBST*self.isValidBST(root.left)*self.isValidBST(root.right)

