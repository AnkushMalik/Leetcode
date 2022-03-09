class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    uf.union(i,j)
        return len(set(uf.group))
        
class UnionFind:
    def __init__(self,size):
        self.group = [i for i in range(size)]
    
    def find(self, node):
        if node!=self.group[node]:
            node = self.find(self.group[node])
        return node
    
    def union(self, a, b):
        grp_a = self.group[a]
        grp_b = self.group[b]
        
        if grp_a!=grp_b:
            for i in range(len(self.group)):
                if self.group[i]==grp_b:
                    self.group[i]=grp_a