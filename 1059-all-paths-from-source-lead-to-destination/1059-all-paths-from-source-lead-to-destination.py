class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges: return source==destination # check graph doesnt have any edges
        adjList = {}
        for p,q in edges:
            if p==destination: return False # check "no outgoing edges" from destination
            if p not in adjList: adjList[p]=[]
            if q not in adjList: adjList[q]=[]
            adjList[p].append(q)

        def dfs(node):
            if node==destination: return True
			# if adjList[node] is empty and node !=destination OR all neighbouring nodes are visited('X') return False
            elif not adjList[node] or adjList[node].count('X')==len(adjList[node]): return False 
            for i in range(len(adjList[node])):
                nbr = adjList[node][i]
                if nbr==node: return False # if a infinite loop is present in the path then return False
                if nbr=='X': continue # marking visited nodes 
                adjList[node][i]='X'
                if not dfs(nbr): return False # if couldnt reach destination instant return False
                adjList[node][i]=nbr # remarking it to original value; removing visited mark for other paths to use this node again.
            return True # if no failure in above loop checks, finally return True
        return dfs(source)