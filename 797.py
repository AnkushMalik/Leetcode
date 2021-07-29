'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.tracePath(graph,[0],len(graph)-1)
        return self.paths

    def tracePath(self, graph, path, dest):
        if path[-1]==dest:
            self.paths.append(path[:])
            return
        else:
            for vertice in graph[path[-1]]:
                if vertice not in path:
                    path.append(vertice)
                    self.tracePath(graph,path,dest)
                    path.pop()
