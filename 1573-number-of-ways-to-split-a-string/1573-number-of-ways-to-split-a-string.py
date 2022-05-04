class Solution:
    def numWays(self, s: str) -> int:
        ones = [i for i in range(len(s)) if s[i]=='1']
        if len(ones)%3!=0: return 0
        if len(ones)==0:
            n = len(s)
            return ((n-1)*(n-2)//2)%(10**9+7)
        i = len(ones)//3
        j = 2*i
        count = (ones[i]-ones[i-1])*(ones[j]-ones[j-1])
        return count%(10**9+7)