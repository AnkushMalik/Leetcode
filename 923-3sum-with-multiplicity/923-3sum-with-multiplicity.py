class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        seen = {
            arr[0]: 1
        }
        count = 0
        for j in range(1,len(arr)-1):
            for k in range(j+1, len(arr)):
                twosum =  arr[j]+arr[k]
                if twosum>target: continue
                else:
                    thirdNum = target-twosum
                    if thirdNum in seen:
                        count+=seen[thirdNum]
            if arr[j] in seen: seen[arr[j]]+=1
            else: seen[arr[j]]=1
        return count%(10**9+7)