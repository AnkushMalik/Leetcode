class Solution:
    def hammingWeight(self, n: int) -> int:
        ct=0
        while n:
            ct+=n%2
            n//=2
        return ct