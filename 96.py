'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
'''

class Solution:
    hsh = {0:1,1:1}
    def numTrees(self, n: int) -> int:
        count = 0
        for i in range(0,n):
            if i not in self.hsh:
                self.hsh[i] = self.numTrees(i)
            if n-i-1 not in self.hsh:
                self.hsh[n-i-1] = self.numTrees(n-i-1)
            count+=self.hsh[i]*self.hsh[n-i-1]
        return count
