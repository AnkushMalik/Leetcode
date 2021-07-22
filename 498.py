'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hsh = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                itr = i+j
                if itr in hsh:
                    if itr%2==0:
                        hsh[itr].insert(0,mat[i][j])
                    else:
                        hsh[itr].append(mat[i][j])     
                else:
                    hsh[itr]=[mat[i][j]]
        ans = []
        for i in hsh.values():
            ans+=i
        return ans
