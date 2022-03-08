class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        timeline = sorted(logs,key=lambda d: d[0])
        uf = UnionFind(n)
        
        for time, a, b in timeline:
            isNewFriendship = uf.union(a,b)
            if isNewFriendship:
                if len(set(uf.group))==1: return time
        return -1

class UnionFind:
    def __init__(self,size):
        self.group = [i for i in range(size)]
    
    def find(self,node):
        while(node!=self.group[node]):
            node = self.group[node]
        return node
    
    def union(self,a,b):
        grp_a = self.find(a)
        grp_b = self.find(b)
        
        if grp_a==grp_b: return False
        
        for i in range(len(self.group)):
            if self.group[i]==grp_b:
                self.group[i]=grp_a
        return True
            