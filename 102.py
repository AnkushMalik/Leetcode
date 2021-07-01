'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        lvl = []
        result = []
        next_que = []
        que = [root]
        while(len(que)!=0):
            for i in que:
                lvl.append(i.val)
                if i.left:
                    next_que.append(i.left)
                if i.right:
                    next_que.append(i.right)
            result.append(lvl)
            que = next_que
            lvl = []
            next_que = []
        return result
