class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i]= ans[i//2] if i%2==0 else ans[i//2]+1
        return ans
# 0 : 0
# 1 : 1
# 2 :10
# 3 :11
# 4 :100
# 5 :101
# 6 :110
# 7 :111
# 8 :1000
# 9 :1001
# 10:1010
# 11:1011
# 12:1100
# 13:1101
# 14:1110
# 15:1111
# 16:10000