class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        curr_profit = 0
        day = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<day:
                day = prices[i]
            else:
                curr_profit = prices[i]-day
                maxprofit = max(maxprofit,curr_profit)
        return maxprofit