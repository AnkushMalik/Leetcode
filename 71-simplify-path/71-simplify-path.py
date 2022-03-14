class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = ''
        stk = []
        temp = path.split('/')
        for i in temp:
            if len(i)>0:
                if i=='..':
                    if stk: stk.pop()
                elif i!='.':
                    stk.append(i)
        for i in stk:
            ans+='/'+i
        return ans if len(ans) else '/'