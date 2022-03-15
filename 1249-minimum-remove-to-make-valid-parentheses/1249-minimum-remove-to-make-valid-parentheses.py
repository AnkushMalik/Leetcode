class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        ans = ''
        for i in range(len(s)):
            if not s[i].isalpha():
                if s[i]=='(':
                    stk.append(i)
                else:
                    if stk and s[stk[-1]]=='(': stk.pop()
                    else:
                        stk.append(i)
        for i in range(len(s)):
            if i not in stk:
                ans+=s[i]
        return ans