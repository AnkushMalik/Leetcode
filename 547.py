'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

'''
class DisjointSet:
    def __init__(self,size):
        self.count=size
        self.root = [i for i in range(size)]
        self.rank = [1]*size

    def find(self,x):
        if x ==self.root[x]: return self.root[x]
        self.root[x]=self.find(self.root[x])
        return self.root[x]

    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rooty]>self.rank[rootx]:   
                self.root[rootx] = rooty
            else:
                self.root[rooty]=rootx
                self.rank[rootx]+=1
            self.count-=1
        
    def getGraphCount(self):
        return self.count
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        djs = DisjointSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    djs.union(i,j)
        return djs.getGraphCount()
