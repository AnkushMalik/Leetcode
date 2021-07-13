'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        if len(postorder)==1:
            return TreeNode(postorder[0])
        
        root = TreeNode(postorder.pop())
        pt = inorder.index(root.val) 
        ltInOrder = inorder[:pt]
        rtInOrder = inorder[pt+1:]
        
        ltPostOrder = postorder[:len(ltInOrder)]
        rtPostOrder = postorder[len(ltInOrder):]
        
        root.left =  self.buildTree(ltInOrder,ltPostOrder)
        root.right = self.buildTree(rtInOrder,rtPostOrder)
        return root
        
