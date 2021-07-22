'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
'''

class Solution:
    hsh = {'[]':[None]}
    def generateTrees(self, n: int) -> List[TreeNode]:
        ret = self.findAllTrees(list(range(1,n+1)))
        return ret
    
    def findAllTrees(self, arr):
        if len(arr)==1: return [TreeNode(arr[0])]
        if str(arr) in self.hsh: return self.hsh[str(arr)]
        else:
            ret = []
            for i in range(len(arr)):
                left = arr[:i]
                right = arr[i+1:]
                if str(left) not in self.hsh:
                    self.hsh[str(left)] = self.findAllTrees(left)
                if str(right) not in self.hsh:
                    self.hsh[str(right)] = self.findAllTrees(right)
                
                for lt in self.hsh[str(left)]:
                    for rt in self.hsh[str(right)]:
                        root = TreeNode(arr[i])
                        root.left = lt
                        root.right = rt
                        ret.append(root)
            self.hsh[str(arr)] = ret
        return self.hsh[str(arr)]
