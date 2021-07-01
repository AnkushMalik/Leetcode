'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if(root==None):
            return None
            
        if(root.left==None and root.right==None):
            return [root.val]
        
        ans = []

        if(root.left):
            ans+=self.inorderTraversal(root.left)
        ans += [root.val]
        if(root.right):
            ans+=self.inorderTraversal(root.right)

        return ans
