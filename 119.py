'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]*(rowIndex+1)
        if(rowIndex<=1):
            return ans
        
        prevrow = self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            ans[i]=prevrow[i-1]+prevrow[i]
        return ans

