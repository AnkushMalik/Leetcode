class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        ans = [-1]*len(workers)
        pairs = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                hamDist = abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
                pairs.append([hamDist,i,j])
        pairs.sort()
        i = 0
        for d,w,b in pairs:
            if ans[w]==-1 and bikes[b]!='X':
                ans[w]=b
                bikes[b]='X'
                i+=1
            if i==len(workers): break
        return ans