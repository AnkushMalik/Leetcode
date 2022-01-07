class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.ans = []
        self.findAllComb(s,0)
        return self.ans
    
    def findAllComb(self, s, i):
        if i==len(s):
            self.ans.append(s)
        else:
            if s[i].isdigit():
                self.findAllComb(s,i+1)
            else:
                self.findAllComb(s[:i]+s[i].upper()+s[i+1:],i+1)
                self.findAllComb(s[:i]+s[i].lower()+s[i+1:],i+1)