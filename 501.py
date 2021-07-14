'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
'''
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.nodash = {}
        self.findFreq(root)
        mode = [0]
        maxFreq = [0]
        for k,v in self.nodash.items():
            if v>maxFreq[0]:
                maxFreq = [v]
                mode = [k]
            elif v==maxFreq[0]:
                maxFreq.append(v)
                mode.append(k)
        return mode
    def findFreq(self,root):
        if not root: return
        if root.val in self.nodash:
            self.nodash[root.val]+=1
        else:
            self.nodash[root.val]=1
        self.findFreq(root.left)
        self.findFreq(root.right)
