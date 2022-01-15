class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = []
        for i in matrix: mat+=i
        start = 0
        end = len(mat)-1
        mid = (start+end)//2
    
        while(start<=end):
            if target==mat[mid] or target==mat[start] or target ==mat[end]:
                return True
            elif target<mat[mid]:
                end = mid-1
            elif target>mat[mid]:
                start = mid+1
            mid = (start+end)//2
        return False