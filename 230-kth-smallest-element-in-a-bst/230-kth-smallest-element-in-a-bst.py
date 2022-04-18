# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hp = []
        heapify(hp)
        def dfs(node):
            if not node: return
            heappush(hp, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        for i in range(k):
            kelem = heappop(hp)
            if i==k-1:
                return kelem
        return root.val