class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        lastOcc = {c:i for i,c in enumerate(s)}
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                while stk and i<lastOcc[stk[-1]] and stk[-1]>s[i]:
                    seen.discard(stk.pop())
                stk.append(s[i])
                seen.add(s[i])
        return ''.join(stk)
            