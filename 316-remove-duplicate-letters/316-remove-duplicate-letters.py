class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        lastOcc = {c:i for i,c in enumerate(s)}
        for i in range(len(s)):
            if s[i] not in stk:
                while stk and i<lastOcc[stk[-1]] and stk[-1]>s[i]:
                    stk.pop()
                stk.append(s[i])
        return ''.join(stk)
            