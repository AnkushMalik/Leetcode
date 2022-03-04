class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        while(n):
            num = 0
            if n in history: return False
            history.append(n)
            while(n>0):
                num+=(n%10)**2
                n = n//10
            if num==1: return True
            n = num
        return False