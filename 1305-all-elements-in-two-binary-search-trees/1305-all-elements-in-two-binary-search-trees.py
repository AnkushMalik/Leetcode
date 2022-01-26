# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr = []
        def dfs(root):
            if not root: return
            arr.append(root.val)
            if root.left: dfs(root.left)
            if root.right: dfs(root.right)
        dfs(root1)
        dfs(root2)
        return sorted(arr)