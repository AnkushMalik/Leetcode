'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: n = 3, trust = [[1,2],[2,3]]
Output: -1
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust: return 1 if n==1 else -1
        hsh = {}
        countHsh = {}
        for u,v in trust:
            if u in hsh: hsh[u].append(v)
            else: hsh[u]=[v]
        
        for u,v in trust:
            if v not in hsh:
                if v not in countHsh: countHsh[v]=1
                else: countHsh[v]+=1
        for u,v in countHsh.items():
            if v==n-1: return u
        return -1
