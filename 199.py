'''
199. Binary Tree Right Side View
Medium

4422

235

Add to List

Share
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        stk = [root]
        ans = []
        while stk:
            ans.append(stk[-1].val)
            for _ in range(len(stk)):
                elem = stk.pop()
                if elem.right:
                    stk.insert(0,elem.right)
                if elem.left:
                    stk.insert(0,elem.left)

        return ans