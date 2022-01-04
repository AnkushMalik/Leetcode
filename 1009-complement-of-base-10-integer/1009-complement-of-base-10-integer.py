class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit = self.findBits(n)
        return self.getComplement(bit)
    def findBits(self,n):
        temp = ""
        while(n>=2):
            temp = str(n%2)+temp
            n=n//2
        temp = str(n)+temp
        return temp
    
    def getComplement(self,s):
        s = list(s)
        for i in range(len(s)):
            s[i]= '1' if s[i]=='0' else '0'
        num = 0
        for i in range(len(s)):
            num+= int(s[i])*(2**(len(s)-i-1))
        return num
            
            