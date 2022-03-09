class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        timeline = sorted(logs,key=lambda d: d[0])
        uf = UnionFind(n)
        
        grp_count = n
        for time, a, b in timeline:
            isNewFriendship = uf.union(a,b)
            print(uf.group)
            if isNewFriendship:
                grp_count-=1
                if grp_count==1: return time
        return -1

class UnionFind:
    def __init__(self,size):
        self.group = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def find(self,node):
        if(node!=self.group[node]):
            node = self.find(self.group[node])
        return node
    
    def union(self,a,b):
        grp_a = self.find(a)
        grp_b = self.find(b)
        
        if grp_a==grp_b: return False
        
        if self.rank[grp_a]>self.rank[grp_b]:
            self.group[grp_b] = grp_a
        elif self.rank[grp_b]>self.rank[grp_a]:
            self.group[grp_a] = grp_b
        else:
            self.group[grp_b]=grp_a
            self.rank[grp_a]+=1
        return True