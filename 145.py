'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
'''

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if(root==None):
            return None
            
        if(root.left==None and root.right==None):
            return [root.val]
        
        ans = []

        if(root.left):
            ans+=self.postorderTraversal(root.left)
        if(root.right):
            ans+=self.postorderTraversal(root.right)
        ans += [root.val]

        return ans
