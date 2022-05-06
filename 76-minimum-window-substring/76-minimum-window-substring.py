class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j  = 0, len(s)-1
        if len(t)>len(s): return ''
        while(i<j):
            if s[i] in t and s[j] in t: break
            if s[i] not in t: i+=1
            if s[j] not in t: j-=1
        s = s[i:j+1]
        h1, h2 = [0]*58, [0]*58
        setS = set(s)
        for i in t:
            if i not in setS: return ''
            h2[ord(i)-ord('A')]+=1
        # for i in s: h1[ord(i)-ord('A')]+=1

        def isValid(h):
            for i in range(58):
                if h2[i] and h2[i]>h[i]: return False
            return True
        
        ans = s
        stk = []
        wasEverChanged = False
        for i in range(len(s)):
            idx = ord(s[i])-ord('A')
            h1[idx]+=1
            stk.append(s[i])
            check = isValid(h1)
            while(check):
                wasEverChanged = True
                if len(stk)<len(ans): ans = ''.join(stk)
                elem = stk.pop(0)
                eid = ord(elem) - ord('A')
                h1[eid] -= 1
                check = isValid(h1)
        return ans if wasEverChanged else ''
                
                
                
                
            