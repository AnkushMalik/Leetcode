class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h1, h2, ans, stk = {},{}, s+t, []
        for i in t:
            if i in h2: h2[i]+=1
            else: h2[i]=1
        def isValid(h):
            for i in h2: 
                if i not in h or h2[i]>h[i]: return False
            return True
        for i in range(len(s)):
            if s[i] in h1: h1[s[i]]+=1
            else: h1[s[i]]=1
            stk.append(s[i])
            check = isValid(h1)
            while(check):
                if len(stk)<len(ans): ans = ''.join(stk)
                h1[stk.pop(0)] -= 1
                check = isValid(h1)
        return ans if len(ans)<=len(s) else ''