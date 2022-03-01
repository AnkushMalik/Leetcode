class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i]= ans[i//2] if i%2==0 else ans[i//2]+1
        return ans