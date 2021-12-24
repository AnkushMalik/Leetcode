class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=end=0
        for i in range(len(s)):
            maxL = max(self.expandFromMiddle(s,i,i),self.expandFromMiddle(s,i,i+1))
            if maxL>end-start:
                start = i-(maxL-1)//2
                end = i+(maxL)//2
        return s[start:end+1]

    def expandFromMiddle(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            r+=1
            l-=1
        return r-l-1