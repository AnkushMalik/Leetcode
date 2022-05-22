class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        dp[(0,0)]=True
        for i in range(1,len(s)):
            dp[(i,i)] = True
            if s[i]==s[i-1]:
                dp[(i-1,i)]=True
        
        for i in range(3,len(s)+1):
            for j in range(len(s)-i+1):
                start = j
                end = j+i-1
                if (start+1, end-1) in dp and s[start]==s[end]:
                    dp[(start,end)]=True
        
        return len(dp)
        