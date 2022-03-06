class Solution:
    def countOrders(self, n: int) -> int:
        if n==1: return 1
        return ((2*n-1)*n*self.countOrders(n-1))%(10**9+7)