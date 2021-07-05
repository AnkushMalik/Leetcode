'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []

'''

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val==val:
            return root
        if not root or (not root.left and not root.right and root.val!=val):
            return None
        return self.searchBST(root.left,val) if val<root.val else self.searchBST(root.right,val)
            
