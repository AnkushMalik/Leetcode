class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjHash = {}

        for i in range(len(equations)):
            x,y = equations[i]
            val = values[i]
            if x not in adjHash: adjHash[x]=[]
            if y not in adjHash: adjHash[y]=[]
            adjHash[x].append([y,val])
            adjHash[y].append([x,1/val])
        
        def findValue(node,toFind,prod,visited):
            if node==toFind: return prod
            temp = -1
            for nbr in adjHash[node]:
                nbr_node,val = nbr
                if visited[nbr_node]: continue
                visited[nbr_node]=True
                temp = max(findValue(nbr_node,toFind,prod*val,visited ),temp)
                visited[nbr_node]=False
            return temp

        res = [-1]*len(queries)
        for i in range(len(queries)):
            x,y = queries[i]
            if x not in adjHash or y not in adjHash: continue
            visited = {k:False for k in adjHash}
            res[i] = findValue(x,y,1,visited)
        return res