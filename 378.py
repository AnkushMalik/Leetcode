'''
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5

'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hsh = {}
        for i in matrix:
            for j in i:
                if j not in hsh:
                    hsh[j]=1
                else:
                    hsh[j]+=1
        srt_keys = sorted(hsh.items(),key= lambda x: x[0])
        count = 0
        for key,val in srt_keys:
            count += val
            if count>=k:
                return key

# using Binary Search:
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         return self.findKthSmallest(matrix,matrix[0][0],matrix[-1][-1],k)

#     def findKthSmallest(self,matrix,minE,maxE,k):
#         if minE>=maxE:
#             return minE
#         mid = minE+(maxE-minE)//2
        
#         relevantElem = []
        
#         for j in range(len(matrix[0])):
#             for i in range(len(matrix)-1,-1,-1):
#                 if matrix[i][j]<minE: break
#                 if matrix[i][j]<=mid: relevantElem.insert(len(relevantElem),matrix[i][j])

#         rec = len(relevantElem)
#         if k==rec:
#             return max(relevantElem)
#         elif k<rec:
#             return self.findKthSmallest(matrix,minE,mid,k)
#         else:
#             return self.findKthSmallest(matrix,mid+1,maxE,k-rec)
