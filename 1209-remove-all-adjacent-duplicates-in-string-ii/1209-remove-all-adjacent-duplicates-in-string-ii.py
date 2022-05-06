class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [0]*len(s)
        i = 1
        stk[0] = 1
        while(i<len(s)):
            if s[i]==s[i-1]:
                stk[i] = stk[i-1]+1
            else:
                stk[i] = 1
            
            if stk[i]==k:
                s = s[:i-k+1]+s[i+1:]
                i = i-k+1
            else:
                i+=1
        return s
                
                    
                
                        