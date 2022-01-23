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
            for i in range(len(stk)):
                if stk[i]==u:
                    return stk[i+1] if i!=len(stk)-1 else None
            temp = []
            for i in stk:
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            stk = temp
        return None