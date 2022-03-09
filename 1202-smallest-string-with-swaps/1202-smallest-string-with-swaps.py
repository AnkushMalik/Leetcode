class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for p1,p2 in pairs:
            uf.union(p1, p2)
        pg = uf.grp
        hsh = {}
        res = [None]*len(s)
        for i in range(len(s)):
            root = uf.find(i)
            if root in hsh:
                hsh[root]+=[i]
            else:
                hsh[root]=[i]
        for i in hsh:
            keys = hsh[i]
            value = [s[k] for k in keys]
            value.sort()
            for k in range(len(keys)):
                res[keys[k]]=value[k]
        return ''.join(res)

class UnionFind:
    def __init__(self, size):
        self.grp = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
        
    def find(self,node):
        if node != self.grp[node]:
            node = self.find(self.grp[node])
        return node
    
    def union(self, a, b):
        grp_a = self.find(a)
        grp_b = self.find(b)
        
        if grp_a!=grp_b:
            if self.rank[grp_a]>self.rank[grp_b]:
                self.grp[grp_b]=grp_a
            elif self.rank[grp_a]<self.rank[grp_b]:
                self.grp[grp_a]=grp_b
            else:
                self.grp[grp_b]=grp_a
                self.rank[grp_a]+=1
            