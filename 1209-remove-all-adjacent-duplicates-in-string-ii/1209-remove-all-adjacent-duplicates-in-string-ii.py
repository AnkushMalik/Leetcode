class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 1
        stk = [1]
        while(i<len(s)):
            if i == 0: i=1
            if not stk: stk = [1]
            if s[i]==s[i-1]:
                stk[-1]+=1
            else:
                stk.append(1)
            
            if stk[-1]==k:
                s = s[:i-k+1]+s[i+1:]
                i = i-k+1
                stk.pop()
            else:
                i+=1
        return s