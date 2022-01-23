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
            for i in range(len(stk)):
                if stk[i]==u:
                    return stk[i+1] if i!=len(stk)-1 else None
                else:
                    if stk[i].left: temp.append(stk[i].left)
                    if stk[i].right: temp.append(stk[i].right)
            stk = temp
        return None