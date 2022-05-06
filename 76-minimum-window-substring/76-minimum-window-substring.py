class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h1, h2 = [0]*58, [0]*58        
        for i in t:
            if i not in s: return ''
            h2[ord(i)-ord('A')]+=1

        def isValid(h):
            for i in range(58):
                if h2[i] and h2[i]>h[i]: return False
            return True
        
        ans = s+t
        stk = []
        for i in range(len(s)):
            idx = ord(s[i])-ord('A')
            h1[idx]+=1
            stk.append(s[i])
            check = isValid(h1)
            while(check):
                if len(stk)<len(ans): ans = ''.join(stk)
                elem = stk.pop(0)
                eid = ord(elem) - ord('A')
                h1[eid] -= 1
                check = isValid(h1)
        return ans if len(ans)<=len(s) else ''
                
                
                
                
            