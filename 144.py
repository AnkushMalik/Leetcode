'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
'''

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if(root==None):
            return None
            
        if(root.left==None and root.right==None):
            return [root.val]
        
        ans = []
        ans += [root.val]

        if(root.left):
            ans+=self.preorderTraversal(root.left)

        if(root.right):
            ans+=self.preorderTraversal(root.right)

        return ans
