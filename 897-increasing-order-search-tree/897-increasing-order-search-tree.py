# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = TreeNode()
        ptr = self.ans
        def dfs(node):
            if not node: return node
            dfs(node.left)
            self.ans.right = TreeNode(node.val)
            self.ans = self.ans.right
            dfs(node.right)
        dfs(root)
        return ptr.right