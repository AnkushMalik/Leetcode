class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        s_as = self.alphaSign(s)
        t_as = self.alphaSign(t)
        return s_as==t_as
        
    def alphaSign(self,s):
        alpha = [0]*26
        for i in s: alpha[ord(i)-ord('a')]+=1
        return alpha