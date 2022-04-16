class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        pways = total//cost1 + 1 # number of ways of buying pens; "+1" for buying 0 pen.
        for i in range(pways):
            mleft = total - cost1*i # money left after buying i pens
            ans += (mleft//cost2 +1) # similarly, number of ways for buying pencils from ammount left.
        return ans