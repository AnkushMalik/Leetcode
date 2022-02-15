class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = 0
        for i in range(len(s)-k+1):
            subs = s[i:i+k]
            if self.checkMapper(subs): count+=1
        return count
    def checkMapper(self,s):
        hsh = {}
        for i in s:
            if i in hsh:
                return False
            hsh[i] = None
        return True
        