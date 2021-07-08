'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = self.findGoodNodes(root,[])
        return ans

    def isGoodNode(self, value, path):
        for x in path:
            if x>value: return False
        return True

    def findGoodNodes(self, root, path):
        if not root.left and not root.right:
            if self.isGoodNode(root.val, path): return 1
            return 0
        
        ans = 1 if self.isGoodNode(root.val, path) else 0
        path.append(root.val)
        ans+= self.findGoodNodes(root.left, path) if root.left else 0
        ans+= self.findGoodNodes(root.right, path) if root.right else 0
        path.pop()

        return ans
