class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        temp = path.split('/')
        for i in temp:
            if len(i)>0:
                if i=='..':
                    if stk: stk.pop()
                elif i!='.':
                    stk.append(i)
        return '/'+'/'.join(stk)