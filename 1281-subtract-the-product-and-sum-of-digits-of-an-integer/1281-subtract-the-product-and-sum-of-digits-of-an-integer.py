class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sm = 0
        prd = 1
        for i in str(n):
            sm+=int(i)
            prd*=int(i)
        return prd-sm