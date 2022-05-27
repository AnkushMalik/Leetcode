class Solution:
    def numberOfSteps(self, n: int) -> int:
        if n==0: return 0
        return 1+self.numberOfSteps(n//2) if n%2==0 else 1+self.numberOfSteps(n-1)
            