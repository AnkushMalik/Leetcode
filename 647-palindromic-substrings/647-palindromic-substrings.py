class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = set((0,0))
        for i in range(1,len(s)):
            dp.add((i,i))
            if s[i]==s[i-1]:
                dp.add((i-1,i))
        
        for i in range(3,len(s)+1):
            for j in range(len(s)-i+1):
                start = j
                end = j+i-1
                if (start+1, end-1) in dp and s[start]==s[end]:
                    dp.add((start,end))
        return len(dp)
        