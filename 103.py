'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 


'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        stk1= [root]
        stk2= []
        lvl = []
        ans = []
        while stk1 or stk2:
            while(stk1):
                node = stk1.pop()
                lvl.append(node.val)
                if node.left: stk2.append(node.left)
                if node.right: stk2.append(node.right)
            ans.append(lvl)
            lvl = []
            while(stk2):
                node = stk2.pop()
                lvl.append(node.val)
                if node.right: stk1.append(node.right)
                if node.left: stk1.append(node.left)
            if lvl: ans.append(lvl)
            lvl=[]
        return ans
