class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [0]*n
        for i in trust:
            arr[i[0]-1]+=1
            arr[i[1]-1]-=1
        for i in range(n):
            if arr[i]-1==-n:
                return i+1
        return -1
                