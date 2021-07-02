'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
'''

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lCount = self.maxDepth(root.left) if root.left else 0
        rCount = self.maxDepth(root.right) if root.right else 0
        return 1+max(lCount,rCount)
