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
        