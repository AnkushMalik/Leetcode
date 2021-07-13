'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
'''
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stk = [root]
        ans = root.val
        if ans==target: return ans
        diff = 10**9
        
        while stk!=[]:
            node = stk.pop()
            nodeDiff = abs(node.val-target)
            if nodeDiff<diff:
                ans = node.val
                diff = nodeDiff

            if node.val==target: return node.val
            elif node.val<target: 
                if node.right: stk.append(node.right)
            else: 
                if node.left: stk.append(node.left)
        return ans
