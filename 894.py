'''
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
'''

class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n%2==0: return []
        self.memo = {}
        self.findAllFBT(n)
        if n in self.memo:
            return self.memo[n]
        else:
            return []
        
    def findAllFBT(self,n):
        if n%2==0: return
        if n in self.memo: return
        if n==1: 
            self.memo[1]=[TreeNode(0)]
            return
        
        res = []
        for i in range(1,n):
            leftNodes = i-1
            rightNodes = n-i
            
            if leftNodes%2!=0 and rightNodes%2!=0:
                self.findAllFBT(leftNodes)
                self.findAllFBT(rightNodes)
                leftTrees = self.memo[leftNodes]
                rightTrees = self.memo[rightNodes]
                for lt in leftTrees:
                    for rt in rightTrees:
                        root = TreeNode(0,lt,rt)
                        res.append(root)
        self.memo[n]=res

