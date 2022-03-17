class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = {}
        for to,frm in tickets:
            if to not in adjList: adjList[to]=[]
            if frm not in adjList: adjList[frm]=[]
            adjList[to].append(frm)
        for key in adjList: adjList[key] = sorted(adjList[key])
        n = len(tickets)+1
        itr = ['JFK']
        def dfs(node):
            for i in range(len(adjList[node])):
                nbr = adjList[node][i]
                if nbr=='X': continue
                adjList[node][i] = 'X'
                itr.append(nbr)
                if dfs(nbr):
                    break
                itr.pop()
                adjList[node][i] = nbr
            return len(itr)==n
        dfs('JFK')
        return itr