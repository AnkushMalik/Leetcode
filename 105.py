'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder)==1:
            return TreeNode(preorder.pop(0))
        rootVal = preorder.pop(0)
        leftSubtreeInorder = inorder[:inorder.index(rootVal)]
        rightSubtreeInorder = inorder[inorder.index(rootVal)+1:]
        
        leftSubtreePreorder = preorder[:len(leftSubtreeInorder)]
        rightSubtreePreorder = preorder[len(leftSubtreeInorder):]
        
        root = TreeNode(rootVal)
        root.left = self.buildTree(leftSubtreePreorder,leftSubtreeInorder)
        root.right = self.buildTree(rightSubtreePreorder,rightSubtreeInorder)
        
        return root
