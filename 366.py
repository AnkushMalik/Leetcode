'''
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
'''

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        total_leaves = []
        while root.left or root.right:
            level = [root]
            leaves = []
            next_que = []
            while(len(level)!=0):
                for i in level:
                    ndL = i.left
                    ndR = i.right

                    if(ndL and not ndL.left and not ndL.right):
                        #ndl exists and it is a leaf
                        leaves.append(ndL.val)
                        i.left=None #delete left node after appending

                    if(ndR and not ndR.left and not ndR.right):
                        #ndR exists and it is a leaf
                        leaves.append(ndR.val)
                        i.right=None #delete left node after appending

                    if i.left: next_que.append(i.left)
                    if i.right: next_que.append(i.right)
                level = next_que
                next_que = []
            total_leaves.append(leaves)
        total_leaves.append([root.val])
        return total_leaves
        
