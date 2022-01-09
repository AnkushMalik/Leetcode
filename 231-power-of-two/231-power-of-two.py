class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0: return False
        count = 0
        while n:
            if n%2: count+=1
            n=n//2
        return True if count==1 else False