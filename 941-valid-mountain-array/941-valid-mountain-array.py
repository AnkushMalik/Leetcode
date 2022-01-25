class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        maxi = arr.index(max(arr))
        if maxi==0 or maxi==len(arr)-1: return False
        for i in range(1,maxi):
            if arr[i]-arr[i-1]<=0:return False
        for i in range(maxi+1,len(arr)):
            if arr[i]-arr[i-1]>=0: return False
        return True