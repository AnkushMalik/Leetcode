'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)
        
        height = 0
        if not leftHeight or not rightHeight:
            return 1 + leftHeight + rightHeight
        else:
            return 1 + min(leftHeight,rightHeight)
