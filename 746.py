'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stepCount = {}
        def findLowestCost(cost, j=0):
            if j>=len(cost)-1: return 0
            if j in stepCount: return stepCount[j]
            else:
                firstStep = cost[j]+findLowestCost(cost,j+1)
                secondStep = cost[j+1]+findLowestCost(cost,j+2)
                stepCount[j]=min(firstStep,secondStep)
                return stepCount[j]
        return findLowestCost(cost)
        
