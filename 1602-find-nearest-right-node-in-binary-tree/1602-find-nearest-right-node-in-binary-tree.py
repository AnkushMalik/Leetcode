# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        stk = [root]
        while stk:
            temp = []
            while stk:
                node = stk.pop(0)
                if node==u:
                    return stk[0] if stk else None
                else:
                    if node.left: temp.append(node.left)
                    if node.right: temp.append(node.right)
            stk = temp
        return None