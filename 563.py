'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

 

Example 1:


Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1
'''

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tiltedTree = self.calcTilt(root)
        return self.sumOfNodes(tiltedTree)
    
    def calcTilt(self, root):
        if not root: return 
        if not root.left and not root.right:
            root.val=0
        else:
            leftSum = self.sumOfNodes(root.left) if root.left else 0
            rightSum = self.sumOfNodes(root.right) if root.right else 0
            root.val = abs(leftSum - rightSum)

            self.calcTilt(root.left)
            self.calcTilt(root.right)

        return root
    def sumOfNodes(self,root):
        if not root:
            return 0
        sumTree = root.val
        sumTree+=self.sumOfNodes(root.left) if root.left else 0
        sumTree+=self.sumOfNodes(root.right) if root.right else 0
        return sumTree

#bad solution; only faster than 5%; could use single recursion with two outputs for sum of node, sum of tilt

