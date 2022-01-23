# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hsh = {}
        def mapTree(node):
            if not node: return
            hsh[k-node.val]=node.val
            if node.left: mapTree(node.left)
            if node.right: mapTree(node.right)
            return
        mapTree(root)
        for i in hsh:
            if hsh[i] in hsh and hsh[i]!=i: return True
        return False