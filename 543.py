'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxEdge = 0
        def calculateMaxEdge(node):
            if not node: return 0
            if not node.left and not node.right:
                return 1
            leftHeight = self.calcHeight(node.left)
            rightHeight = self.calcHeight(node.right)
            path = leftHeight+rightHeight
            if path>self.maxEdge:
                self.maxEdge = path
            calculateMaxEdge(node.left)
            calculateMaxEdge(node.right)
            return
        calculateMaxEdge(root)
            
                
        return self.maxEdge
    def calcHeight(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        maxHeight = 1+ max(self.calcHeight(root.left),self.calcHeight(root.right))
        return maxHeight
