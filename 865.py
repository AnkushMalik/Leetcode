'''
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
'''
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.maxD = self.getDepthOfTree(root,1)
        if self.maxD<=2:
            return root
        else:
            return self.getLCA(root,2)
        return root
    def getDepthOfTree(self,root,curD):
        if not root: return curD
        else:
            lD = self.getDepthOfTree(root.left,curD+1) if root.left else curD
            rD = self.getDepthOfTree(root.right, curD+1) if root.right else curD
            return max(curD,lD,rD)

    def getLCA(self,root,depth):
        if not root.left and not root.right: return root
        leftDepth = self.getDepthOfTree(root.left,depth) if root.left else 0
        rightDepth = self.getDepthOfTree(root.right,depth) if root.right else 0

        if leftDepth==self.maxD and rightDepth == self.maxD:
            return root
        elif leftDepth==self.maxD:
            return self.getLCA(root.left, depth+1)
        else:
            return self.getLCA(root.right, depth+1)
