class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        lastOcc = {c:i for i,c in enumerate(s)}
        seen = set()
        for i in range(len(s)):
            c = s[i]
            if c not in seen:
                while stk and i<lastOcc[stk[-1]] and stk[-1]>c:
                    seen.discard(stk.pop())
                stk.append(c)
                seen.add(c)
        return ''.join(stk)
            