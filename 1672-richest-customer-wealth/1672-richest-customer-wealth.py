class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in accounts:
            if(maxWealth<sum(i)):
                maxWealth=sum(i)
        return maxWealth